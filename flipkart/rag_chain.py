import warnings
import sys
import os
import logging
import re

# Add the project root to Python path when running as script
if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage
from flipkart.config import Config

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class RAGChainBuilder:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.model = ChatGroq(
            model=Config.RAG_MODEL, 
            temperature=0.5,
            api_key=Config.GROQ_API_KEY
        )
        self.history_store = {}

    def _get_history(self, session_id: str) -> BaseChatMessageHistory:
        """Retrieve or create chat history for a session"""
        if session_id not in self.history_store:
            self.history_store[session_id] = ChatMessageHistory()
        return self.history_store[session_id]
    
    def _extract_text_from_message(self, message):
        """Extract text content from BaseMessage or convert to string"""
        if isinstance(message, BaseMessage):
            return message.content
        return str(message)
    
    def _format_docs(self, docs):
        """Format retrieved documents into a structured string"""
        if not docs:
            return "No relevant documents found."
        
        formatted = []
        for i, doc in enumerate(docs, 1):
            title = doc.metadata.get('title', 'Product')
            content = doc.page_content.strip()
            formatted.append(f"{i}. {title}: {content}")
        
        return "\n".join(formatted)
    
    def _format_response(self, raw_response):
        """Post-process response for proper formatting and structure"""
        if hasattr(raw_response, 'content'):
            response_text = raw_response.content
        else:
            response_text = str(raw_response)
        
        # Clean up excessive newlines
        response_text = re.sub(r'\n\n\n+', '\n\n', response_text)
        
        return response_text.strip()
    
    def _retrieve_with_timing(self, x, history_aware_retriever):
        import time
        start_time = time.perf_counter()
        docs = history_aware_retriever.invoke(x)
        elapsed_time = (time.perf_counter() - start_time) * 1000
        logger.info(f"=== VECTOR SEARCH RETRIEVAL LATENCY: {elapsed_time:.2f} ms ===")
        return docs

    def build_chain(self):
        """Build the complete RAG chain with message history and structured responses"""
        retriever = self.vector_store.as_retriever(search_kwargs={"k": 3})

        # Prompt to contextualize the question using chat history
        contextualize_q_prompt = ChatPromptTemplate.from_messages([
            ("system", "Given the chat history and a user question, create a standalone question that can be understood without the chat history. Don't answer the question, just reformulate it if needed and otherwise return it as is."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")
        ])

        # Main QA prompt with structured formatting requirements
        qa_system_prompt = """You are a helpful Flipkart e-commerce product assistant.

IMPORTANT RESPONSE GUIDELINES:
1. Keep responses concise and precise (2-3 sentences for simple queries, max 5-6 for complex ones)
2. Use bold formatting like this: Product Name is in bold
3. Use bullet points (•) for feature lists or product comparisons
4. Use numbered lists (1. 2. 3.) for product recommendations
5. Organize information with clear line breaks between sections
6. Limit product recommendations to 3-5 options maximum
7. Include key details: price range, main features, user ratings if available
8. Be professional and friendly
9. Avoid lengthy paragraphs - structure information for easy scanning
10. If uncertain about information, say "I don't have specific details about that" rather than guessing

CONTEXT (Product Information):
{context}

USER QUESTION:
{input}"""

        qa_prompt = ChatPromptTemplate.from_messages([
            ("system", qa_system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")
        ])

        # Build history-aware retriever that rewrites questions with context
        history_aware_retriever = (
            contextualize_q_prompt 
            | self.model 
            | RunnableLambda(self._extract_text_from_message)
            | retriever
        )

        # Build the QA chain with formatted documents
        question_answer_chain = qa_prompt | self.model

        # Build the complete RAG chain with proper document formatting
        rag_chain = (
            RunnablePassthrough.assign(
                context=lambda x: self._retrieve_with_timing(x, history_aware_retriever)
            )
            | RunnablePassthrough.assign(
                context=lambda x: self._format_docs(x["context"])
            )
            | question_answer_chain
            | RunnableLambda(self._format_response)
        )

        # Return chain with message history support
        return RunnableWithMessageHistory(
            rag_chain,
            self._get_history,
            input_messages_key="input",
            history_messages_key="chat_history",
        )
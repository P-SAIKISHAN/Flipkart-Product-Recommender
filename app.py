from flask import render_template, Flask, request, Response
from prometheus_client import Counter, generate_latest
from flipkart.data_ingestion import DataIngestor
from flipkart.rag_chain import RAGChainBuilder
import logging
import re
from markupsafe import Markup

from dotenv import load_dotenv
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

REQUEST_COUNT = Counter("http_requests_total", "Total HTTP Request")

def markdown_to_html(text):
    """Convert markdown-style formatting to HTML"""
    # Convert **bold** to <b>bold</b>
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    
    # Convert bullet points to HTML list
    text = re.sub(r'• (.+?)(?=\n|$)', r'<li>\1</li>', text)
    text = re.sub(r'(<li>.*?</li>)', r'<ul>\1</ul>', text, flags=re.DOTALL)
    
    # Convert numbered lists
    text = re.sub(r'(\d+\.) (.+?)(?=\n|$)', r'<li>\2</li>', text)
    
    # Convert line breaks to <br>
    text = text.replace('\n', '<br>')
    
    return Markup(text)

def create_app():

    app = Flask(__name__)

    try:
        logger.info("Initializing vector store...")
        vector_store = DataIngestor().ingest(load_existing=True)
        
        logger.info("Building RAG chain...")
        rag_chain = RAGChainBuilder(vector_store).build_chain()
        logger.info("RAG chain built successfully!")
    except Exception as e:
        logger.error(f"Error initializing components: {str(e)}")
        raise

    @app.route("/")
    def index():
        REQUEST_COUNT.inc()
        return render_template("index.html")
    
    @app.route("/get", methods=["POST"])
    def get_response():
        try:
            user_input = request.form.get("msg", "").strip()
            
            if not user_input:
                return {"error": "Empty input"}, 400
            
            logger.info(f"User input: {user_input}")
            
            # Invoke the chain and get the response
            response = rag_chain.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": "user-session"}}
            )
            
            # Extract the content from the response object
            if hasattr(response, 'content'):
                answer = response.content
            else:
                answer = str(response)
            
            # Convert markdown to HTML
            answer_html = markdown_to_html(answer)
            
            logger.info(f"Bot response: {answer}")
            return answer_html
            
        except Exception as e:
            logger.error(f"Error in get_response: {str(e)}")
            import traceback
            traceback.print_exc()
            return {"error": str(e)}, 500
    
    @app.route("/metrics")
    def metrics():
        REQUEST_COUNT.inc()
        return Response(generate_latest(), mimetype="text/plain")
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
from flask import render_template, Flask, request, Response, jsonify
from prometheus_client import Counter, generate_latest
from flipkart.data_ingestion import DataIngestor
from flipkart.rag_chain import RAGChainBuilder
import logging
import re
from markupsafe import Markup
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Metrics
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP Requests")


def markdown_to_html(text):
    """Convert markdown-style formatting to HTML"""

    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)

    # Bullet points
    text = re.sub(r'• (.+?)(?=\n|$)', r'<li>\1</li>', text)

    # Numbered lists
    text = re.sub(r'(\d+\.) (.+?)(?=\n|$)', r'<li>\2</li>', text)

    # Wrap list items
    if "<li>" in text:
        text = f"<ul>{text}</ul>"

    # Line breaks
    text = text.replace('\n', '<br>')

    return Markup(text)


def create_app():
    app = Flask(__name__)

    # -----------------------------
    # Initialize RAG Components
    # -----------------------------
    try:
        logger.info("Initializing vector store...")

        vector_store = DataIngestor().ingest(load_existing=True)

        logger.info("Building RAG chain...")

        rag_chain = RAGChainBuilder(vector_store).build_chain()

        logger.info("RAG chain initialized successfully!")

    except Exception as e:
        logger.exception("Startup initialization failed")
        raise e

    # -----------------------------
    # Routes
    # -----------------------------

    @app.route("/")
    def index():
        REQUEST_COUNT.inc()
        return render_template("index.html")

    @app.route("/health")
    def health():
        return jsonify({
            "status": "healthy"
        }), 200

    @app.route("/get", methods=["POST"])
    def get_response():

        REQUEST_COUNT.inc()

        try:
            user_input = request.form.get("msg", "").strip()

            if not user_input:
                return jsonify({
                    "error": "Input cannot be empty"
                }), 400

            logger.info(f"User Input: {user_input}")

            response = rag_chain.invoke(
                {"input": user_input},
                config={
                    "configurable": {
                        "session_id": "user-session"
                    }
                }
            )

            # Extract response text
            if hasattr(response, "content"):
                answer = response.content
            else:
                answer = str(response)

            logger.info(f"Bot Response: {answer}")

            # Convert markdown to HTML
            answer_html = markdown_to_html(answer)

            return answer_html

        except Exception as e:
            logger.exception("Error generating response")

            return jsonify({
                "error": str(e)
            }), 500

    @app.route("/metrics")
    def metrics():
        REQUEST_COUNT.inc()
        return Response(
            generate_latest(),
            mimetype="text/plain"
        )

    return app


# -----------------------------
# Vercel Entry Point
# -----------------------------
app = create_app()


# -----------------------------
# Local Development
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )
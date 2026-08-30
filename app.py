from flask import Flask, render_template, request, Response, jsonify
from prometheus_client import Counter, generate_latest
from flipkart.data_ingestion import DataIngestor
from flipkart.rag_chain import RAGChainBuilder
from dotenv import load_dotenv
import logging
import os

# Load environment variables
load_dotenv()

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Diagnostics report
try:
    with open("diagnostics.log", "w") as f:
        f.write("--- ENVIRONMENT VARIABLES DIAGNOSTICS ---\n")
        f.write(f"GROQ_API_KEY: {'LOADED' if os.getenv('GROQ_API_KEY') else 'MISSING'}\n")
        f.write(f"ASTRA_DB_API_ENDPOINT: {'LOADED' if os.getenv('ASTRA_DB_API_ENDPOINT') else 'MISSING'}\n")
        f.write(f"ASTRA_DB_APPLICATION_TOKEN: {'LOADED' if os.getenv('ASTRA_DB_APPLICATION_TOKEN') else 'MISSING'}\n")
        f.write(f"ASTRA_DB_KEYSPACE: {os.getenv('ASTRA_DB_KEYSPACE') or 'MISSING'}\n")
        f.write(f"HF_TOKEN: {'LOADED' if os.getenv('HF_TOKEN') else 'MISSING'}\n")
        f.write(f"HUGGINGFACEHUB_API_TOKEN: {'LOADED' if os.getenv('HUGGINGFACEHUB_API_TOKEN') else 'MISSING'}\n")
except Exception as log_err:
    pass

# Prometheus Metrics
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP Requests"
)

# Global RAG chain
rag_chain = None


def get_rag_chain():
    """
    Lazy load the RAG chain.
    Prevents Vercel startup crashes.
    """
    global rag_chain

    if rag_chain is None:
        logger.info("Initializing vector store...")

        vector_store = DataIngestor().ingest(
            load_existing=True
        )

        logger.info("Building RAG chain...")

        rag_chain = RAGChainBuilder(
            vector_store
        ).build_chain()

        logger.info("RAG chain initialized successfully!")

    return rag_chain


def create_app():

    app = Flask(__name__)

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

            # Load chain lazily
            chain = get_rag_chain()

            response = chain.invoke(
                {"input": user_input},
                config={
                    "configurable": {
                        "session_id": "user-session"
                    }
                }
            )

            # Extract answer safely
            if isinstance(response, dict):
                answer = response.get("answer", str(response))
            else:
                answer = str(response)

            logger.info(f"Bot Response: {answer}")

            return answer

        except Exception as e:
            logger.exception("Error generating response")
            import traceback
            try:
                with open("error.log", "w") as f:
                    traceback.print_exc(file=f)
            except Exception as log_err:
                pass

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


# IMPORTANT FOR VERCEL
app = create_app()


# Local development
if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )
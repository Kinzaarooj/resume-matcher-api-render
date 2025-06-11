from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import logging

# ✅ Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ Load environment
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    logger.error("OPENAI_API_KEY not found!")
    raise ValueError("OPENAI_API_KEY not found!")

pinecone_api_key = os.getenv("PINECONE_API_KEY")
if not pinecone_api_key:
    logger.error("PINECONE_API_KEY not found!")
    raise ValueError("PINECONE_API_KEY not found!")

# ✅ Flask App
app = Flask(__name__)

# ✅ Health Check Route (Render checks this!)
@app.route("/", methods=["GET"])
def home():
    logger.info("Health check route accessed")
    return jsonify({"status": "OK", "message": "Webhook is live"}), 200

# ✅ Resume Matcher Endpoint
@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        logger.info(f"Received webhook data: {data}")
        from resume_matcher_jobs import match_resume_to_jobs  # Import inside to avoid startup issues
        result = match_resume_to_jobs(data)
        logger.info(f"Match result: {result}")
        return jsonify({"status": "success", "matches": result}), 200
    except Exception as e:
        logger.error(f"Error in webhook: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    logger.info(f"Starting app on port {port}")
    app.run(host="0.0.0.0", port=port, debug=False)
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from resume_matcher_corrected import match_resume_to_jobs

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in environment!")

# Initialize Flask app
app = Flask(__name__)

# Health check route for Render root URL
@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "OK", "message": "Webhook is live"}), 200

# Webhook route to receive parsed resume JSON
@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        result = match_resume_to_jobs(data)
        return jsonify({"status": "success", "matches": result}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Entry point for Gunicorn
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
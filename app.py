from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from resume_matcher_corrected import match_resume_to_jobs

# ✅ Load environment
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found!")

# ✅ Flask App
app = Flask(__name__)

# ✅ Health Check Route (Render checks this!)
@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "OK", "message": "Webhook is live"}), 200

# ✅ Resume Matcher Endpoint
@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        result = match_resume_to_jobs(data)
        return jsonify({"status": "success", "matches": result}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ✅ Gunicorn Entrypoint for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
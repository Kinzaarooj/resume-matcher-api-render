from flask import Flask, request, jsonify # type: ignore
import os
from resume_matcher_corrected import match_resume_to_jobs  # Make sure this file/function exists

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        resume_json = request.get_json()
        result = match_resume_to_jobs(resume_json)
        return jsonify({"status": "success", "matches": result}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use dynamic port from Render
    app.run(host="0.0.0.0", port=port)
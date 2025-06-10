from flask import Flask, request, jsonify  # type: ignore
from dotenv import load_dotenv
import os
from resume_matcher_corrected import match_resume_to_jobs  # Ensure this file exists

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OpenAI API key not set in .env file")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Resume Matcher Webhook is Live!"

@app.route('/match', methods=['POST'])
def match_resume():
    try:
        data = request.get_json()
        print(f"Received data: {data}")  # Debug log
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        result = match_resume_to_jobs(data)
        return jsonify(result), 200
    except Exception as e:
        print(f"Error in match_resume: {str(e)}")  # Error log
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
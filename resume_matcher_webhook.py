from flask import Flask, request, jsonify # type: ignore
import json
from resume_matcher_corrected import match_resume_to_jobs  # make sure this matches your function name
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Resume Matcher Webhook is Live!"

@app.route('/match', methods=['POST'])
def match_resume():
    try:
        data = request.get_json()

        # Use your matcher logic
        matches = match_resume_to_jobs(data)

        return jsonify({
            "status": "success",
            "matches": matches
        })
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
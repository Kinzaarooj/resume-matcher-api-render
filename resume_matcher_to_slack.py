import json
import requests

# Load parsed resume data
with open("parsed_resume_sample.json", "r", encoding="utf-8") as f:
    resume_data = json.load(f)

# Dummy job matches (simulate Pinecone output)
jobs = [
    {
        "job_title": "AI Engineer",
        "company": "TechNova",
        "location": "Berlin",
        "requirements": ["Python", "GPT", "NLP"],
        "score": 0.92
    },
    {
        "job_title": "Machine Learning Analyst",
        "company": "DataVision",
        "location": "Munich",
        "requirements": ["Pandas", "NumPy", "TensorFlow"],
        "score": 0.88
    }
]

# Prepare message
blocks = []
for job in jobs:
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f"*New Resume Match for:*\n*{job['job_title']}* at *{job['company']}*\n📍 Location: {job['location']}\n📋 Requirements: {', '.join(job['requirements'])}\n⭐ Score: {job['score']:.2f}"
        }
    })
    blocks.append({"type": "divider"})

# Send message to Slack
response = requests.post(
    "https://hooks.slack.com/services/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",
    json={
        "text": "New Resume Matches Found",
        "blocks": blocks
    }
)

print("✅ Sent to Slack:", response.status_code, response.text)
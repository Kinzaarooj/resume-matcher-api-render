import json
import requests

# Load parsed resume data
with open("parsed_resume_sample.json", "r", encoding='utf-8') as f:
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
            "text": f"*New Resume Match for:* {job['job_title']} at *{job['company']}* 📍 Location: {job['location']} 🔍 Requirements: {', '.join(job['requirements'])}"
        }
    })
    blocks.append({"type": "divider"})

# You can integrate with Slack webhook here
print("Slack message prepared:")
print(json.dumps(blocks, indent=2))
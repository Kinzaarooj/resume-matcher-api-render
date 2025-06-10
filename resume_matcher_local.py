import json

# Load parsed resume data from local JSON
with open("parsed_resume_sample.json", "r", encoding="utf-8") as f:
    resume_data = json.load(f)

# Dummy jobs to simulate Pinecone response
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
    },
    {
        "job_title": "Backend Developer",
        "company": "CloudCore",
        "location": "Hamburg",
        "requirements": ["Node.js", "APIs", "MongoDB"],
        "score": 0.72
    }
]

# Print matched jobs
for job in jobs:
    print(f"📌 {job['job_title']} at {job['company']}")
    print(f"📍 Location: {job['location']}")
    print(f"✅ Requirements: {', '.join(job['requirements'])}")
    print(f"⭐ Score: {job['score']:.2f}")
    print("-" * 40)
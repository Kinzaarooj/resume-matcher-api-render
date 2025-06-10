import json
import openai # type: ignore
import os
from pinecone import Pinecone  # type: ignore # ✅ Correct new SDK import

# Load API keys from environment
openai.api_key = os.getenv("OPENAI_API_KEY")
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"), environment="us-west1-gcp")

# Connect to the correct Pinecone index
index = pc.Index("job-matching-index")

# Define function to match resume to jobs
def match_resume_to_jobs(resume_json):
    # Convert structured JSON resume into a string
    resume_text = json.dumps(resume_json)

    # Get embedding from OpenAI
    response = openai.Embedding.create(
        input=resume_text,
        model="text-embedding-ada-002"
    )
    resume_vector = response['data'][0]['embedding']

    # Query Pinecone for best job matches
    query_response = index.query(
        vector=resume_vector,
        top_k=5,
        include_metadata=True
    )

    return query_response
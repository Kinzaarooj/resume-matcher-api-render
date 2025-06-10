import json
import openai
import pinecone
import os

# Make sure your keys are set correctly in Render env vars
openai.api_key = os.getenv("OPENAI_API_KEY")
pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment="us-west1-gcp")

index = pinecone.Index("job-matching-index")

def match_resume_to_jobs(resume_json):
    resume_text = json.dumps(resume_json)

    response = openai.Embedding.create(
        input=resume_text,
        model="text-embedding-ada-002"
    )
    resume_vector = response['data'][0]['embedding']

    query_response = index.query(
        vector=resume_vector,
        top_k=5,
        include_metadata=True
    )

    return query_response
def match_resume_to_jobs(resume_json):
    """
    Match resume to job requirements using simple scoring
    """
    # Sample job database - replace with your actual job matching logic
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
    
    # Extract skills from resume
    resume_skills = resume_json.get('skills', [])
    
    # Simple matching logic
    matched_jobs = []
    for job in jobs:
        job_requirements = job.get('requirements', [])
        
        # Calculate match score
        matches = len(set(resume_skills) & set(job_requirements))
        total_requirements = len(job_requirements)
        
        if total_requirements > 0:
            match_score = matches / total_requirements
            job['match_score'] = round(match_score, 2)
            
        matched_jobs.append(job)
    
    # Sort by match score
    matched_jobs.sort(key=lambda x: x.get('match_score', 0), reverse=True)
    
    return matched_jobs[:5]  # Return top 5 matches
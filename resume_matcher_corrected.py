def match_resume_to_jobs(data):
    try:
        return {
            "data": data,
            "match_score": 0.85
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
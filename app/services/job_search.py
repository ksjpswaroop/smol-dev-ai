```python
from typing import List
from fastapi import HTTPException
from app.models.job import JobSchema
from app.utils.job_search import search_jobs

def search_job(user_id: int, resume_id: int, job_description: str) -> List[JobSchema]:
    try:
        # Fetch the user's resume
        resume = get_resume(user_id, resume_id)
        if not resume:
            raise HTTPException(status_code=404, detail="Resume not found")

        # Search for jobs matching the resume
        jobs = search_jobs(resume, job_description)

        return jobs

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```
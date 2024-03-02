```python
from fastapi import APIRouter, HTTPException, UploadFile, File
from app.services.job_search import search_job
from app.models.job import JobSchema

router = APIRouter()

@router.post("/job_search", response_model=JobSchema)
async def job_search(job_description: str):
    try:
        job = await search_job(job_description)
        if job:
            return {"message": "JOB_SEARCH_SUCCESS", "job": job}
        else:
            raise HTTPException(status_code=404, detail="Job not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```
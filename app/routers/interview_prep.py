```python
from fastapi import APIRouter, HTTPException, UploadFile, File
from app.services.interview_prep import prepare_interview

router = APIRouter()

@router.post("/prepare_interview")
async def interview_prep(job_description: str, resume: UploadFile = File(...)):
    try:
        interview_document = await prepare_interview(job_description, resume)
        return {"message": "INTERVIEW_PREP_SUCCESS", "interview_document": interview_document}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```
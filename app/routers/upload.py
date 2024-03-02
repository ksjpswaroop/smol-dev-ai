```python
from fastapi import APIRouter, UploadFile, File
from app.services.resume_tailoring import tailor_resume

router = APIRouter()

@router.post("/upload/")
async def upload_resume(resume: UploadFile = File(...), job_description: str = ""):
    try:
        tailored_resume = await tailor_resume(resume, job_description)
        return {"message": "UPLOAD_SUCCESS", "tailored_resume": tailored_resume}
    except Exception as e:
        return {"message": str(e)}
```
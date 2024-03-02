```python
from fastapi import HTTPException
from app.models.resume import ResumeSchema
from app.utils.ats_check import check_resume_ats

def check_ats(resume: ResumeSchema):
    try:
        ats_score = check_resume_ats(resume)
        return {"ATS Score": ats_score}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```
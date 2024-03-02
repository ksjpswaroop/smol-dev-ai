```python
from fastapi import APIRouter, HTTPException, UploadFile, File
from app.services.ats_check import check_ats

router = APIRouter()

@router.post("/ats-check")
async def ats_check(resume: UploadFile = File(...)):
    try:
        result = await check_ats(resume)
        return {"message": "ATS_CHECK_SUCCESS", "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```
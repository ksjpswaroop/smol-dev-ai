```python
from fastapi import APIRouter, HTTPException
from app.services.track_applications import track_applications
from app.models.application import ApplicationSchema

router = APIRouter()

@router.post("/track_applications", response_model=ApplicationSchema)
async def track_applications_endpoint(application: ApplicationSchema):
    try:
        result = await track_applications(application)
        return {"message": "TRACK_APPLICATIONS_SUCCESS", "data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```
```python
from typing import List
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.application import ApplicationSchema
from app.db.models import Application

def track_applications(db: Session, user_id: int) -> List[ApplicationSchema]:
    applications = db.query(Application).filter(Application.user_id == user_id).all()
    if not applications:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No applications found for this user.")
    return [ApplicationSchema.from_orm(application) for application in applications]
```
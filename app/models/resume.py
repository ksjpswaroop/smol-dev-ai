```python
from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    content = Column(Text)
    tailored_content = Column(Text)
    ats_score = Column(Integer)
    job_description = Column(Text)
```
```python
from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base

class Interview(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, index=True)
    question = Column(Text)
    answer = Column(Text)

    def __init__(self, job_id, question, answer):
        self.job_id = job_id
        self.question = question
        self.answer = answer
```
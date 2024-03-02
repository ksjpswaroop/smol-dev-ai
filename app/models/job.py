```python
from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    company = Column(String, index=True)
    location = Column(String, index=True)
    description = Column(Text)

    def __init__(self, title, company, location, description):
        self.title = title
        self.company = company
        self.location = location
        self.description = description
```
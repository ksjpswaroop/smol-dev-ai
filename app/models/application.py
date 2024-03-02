from sqlalchemy import Column, Integer, String, DateTime
from app.db.base import Base

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, index=True)
    resume_id = Column(Integer, index=True)
    status = Column(String, default="Submitted")
    submission_date = Column(DateTime)
    response_date = Column(DateTime)
    interview_date = Column(DateTime)
    interview_status = Column(String, default="Pending")
    ats_status = Column(String, default="Pending")
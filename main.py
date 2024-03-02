```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import upload, job_search, interview_prep, ats_check, track_applications
from app.db.session import SessionLocal
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routers
app.include_router(upload.router)
app.include_router(job_search.router)
app.include_router(interview_prep.router)
app.include_router(ats_check.router)
app.include_router(track_applications.router)

@app.on_event("startup")
async def startup_event():
    print("Starting up...")

@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down...")
```
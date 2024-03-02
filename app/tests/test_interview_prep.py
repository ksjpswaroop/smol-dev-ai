```python
import pytest
from fastapi.testclient import TestClient
from main import app
from app.models.interview import InterviewSchema

client = TestClient(app)

def test_prepare_interview():
    response = client.post(
        "/interview_prep/",
        json={
            "resume": "test_resume.pdf",
            "job_description": "Software Engineer at XYZ Corp"
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert "questions" in data
    assert "answers" in data
    assert isinstance(data, InterviewSchema)

def test_prepare_interview_no_resume():
    response = client.post(
        "/interview_prep/",
        json={
            "job_description": "Software Engineer at XYZ Corp"
        },
    )
    assert response.status_code == 400

def test_prepare_interview_no_job_description():
    response = client.post(
        "/interview_prep/",
        json={
            "resume": "test_resume.pdf",
        },
    )
    assert response.status_code == 400
```

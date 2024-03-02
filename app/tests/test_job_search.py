```python
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models.job import JobSchema
from app.services.job_search import search_job

client = TestClient(app)

def test_search_job():
    response = client.post(
        "/job_search/",
        json={"job_description": "Software Engineer", "location": "New York"},
    )
    assert response.status_code == 200
    job_data = JobSchema(**response.json())
    assert job_data.job_description == "Software Engineer"
    assert job_data.location == "New York"

    # Mocking the search_job function to return a specific job
    job = JobSchema(job_description="Software Engineer", location="New York")
    monkeypatch.setattr(search_job, "return_value", job)

    result = search_job("Software Engineer", "New York")
    assert result == job
```
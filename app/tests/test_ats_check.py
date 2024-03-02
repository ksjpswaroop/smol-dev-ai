```python
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.ats_check import check_ats

client = TestClient(app)

def test_check_ats():
    response = client.post(
        "/ats_check/",
        json={
            "resume": "test_resume.pdf",
            "job_description": "Software Engineer"
        },
    )
    assert response.status_code == 200
    assert "ATS_CHECK_SUCCESS" in response.text

    # Test the service function
    result = check_ats("test_resume.pdf", "Software Engineer")
    assert result is not None
    assert isinstance(result, dict)
    assert "ats_score" in result
    assert "feedback" in result
```
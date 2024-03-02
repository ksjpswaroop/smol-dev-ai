```python
from fastapi.testclient import TestClient
from main import app
from app.models.resume import ResumeSchema

client = TestClient(app)

def test_upload_resume():
    resume_data = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "1234567890",
        "skills": ["Python", "FastAPI", "SQL"],
        "experience": [
            {
                "company": "XYZ Corp",
                "role": "Software Developer",
                "duration": "2 years",
                "responsibilities": ["Developed web applications", "Maintained databases"]
            }
        ],
        "education": [
            {
                "institution": "ABC University",
                "degree": "B.Tech in Computer Science",
                "year": "2018"
            }
        ]
    }

    response = client.post("/upload/", json=resume_data)
    assert response.status_code == 200
    assert response.json() == {"message": "UPLOAD_SUCCESS"}

def test_upload_invalid_resume():
    resume_data = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "1234567890",
        "skills": ["Python", "FastAPI", "SQL"],
        "experience": [
            {
                "company": "XYZ Corp",
                "role": "Software Developer",
                "duration": "2 years",
                "responsibilities": ["Developed web applications", "Maintained databases"]
            }
        ],
        # Missing education field
    }

    response = client.post("/upload/", json=resume_data)
    assert response.status_code == 422
```
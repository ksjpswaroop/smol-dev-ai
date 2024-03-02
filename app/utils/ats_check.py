```python
import json
import requests

def check_ats(resume):
    """
    Function to check the ATS score of a resume.
    """
    # ATS API endpoint
    ats_api_url = "https://ats-checker-api.com/check"

    # Prepare the data
    data = {
        "resume": resume
    }

    # Send a POST request to the ATS API
    response = requests.post(ats_api_url, data=json.dumps(data))

    # If the request was successful
    if response.status_code == 200:
        # Parse the response
        ats_score = response.json().get('ats_score')

        # Return the ATS score
        return ats_score

    # If the request was not successful, raise an exception
    else:
        raise Exception("ATS check failed.")
```
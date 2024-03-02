```javascript
document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    let resumeFile = document.getElementById('resumeFile').files[0];
    let jobDescription = document.getElementById('jobDescription').value;
    let formData = new FormData();
    formData.append('resume', resumeFile);
    formData.append('jobDescription', jobDescription);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === 'UPLOAD_SUCCESS') {
            alert('Resume uploaded and tailored successfully!');
        } else {
            alert('There was an error in uploading and tailoring your resume. Please try again.');
        }
    })
    .catch(error => console.error('Error:', error));
});
```
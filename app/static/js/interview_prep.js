document.addEventListener('DOMContentLoaded', (event) => {
    const interviewPrepForm = document.getElementById('interviewPrepForm');
    const jobDescription = document.getElementById('jobDescription');
    const interviewPrepResult = document.getElementById('interviewPrepResult');

    interviewPrepForm.addEventListener('submit', (e) => {
        e.preventDefault();
        fetch('/interview_prep', {
            method: 'POST',
            body: JSON.stringify({
                job_description: jobDescription.value
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                interviewPrepResult.innerText = INTERVIEW_PREP_SUCCESS;
                interviewPrepResult.style.color = 'green';
            } else {
                interviewPrepResult.innerText = data.error;
                interviewPrepResult.style.color = 'red';
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            interviewPrepResult.innerText = 'An error occurred. Please try again.';
            interviewPrepResult.style.color = 'red';
        });
    });
});
document.addEventListener('DOMContentLoaded', (event) => {
    const jobSearchForm = document.getElementById('jobSearchForm');
    jobSearchForm.addEventListener('submit', searchJob);
});

async function searchJob(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const response = await fetch('/job_search', {
        method: 'POST',
        body: formData
    });

    if (response.ok) {
        const data = await response.json();
        if (data.message === 'JOB_SEARCH_SUCCESS') {
            displayJobs(data.jobs);
        } else {
            displayError(data.message);
        }
    } else {
        displayError('An error occurred while searching for jobs.');
    }
}

function displayJobs(jobs) {
    const jobList = document.getElementById('jobList');
    jobList.innerHTML = '';
    jobs.forEach(job => {
        const jobItem = document.createElement('li');
        jobItem.textContent = `${job.title} at ${job.company}`;
        jobList.appendChild(jobItem);
    });
}

function displayError(message) {
    const errorElement = document.getElementById('error');
    errorElement.textContent = message;
    errorElement.style.display = 'block';
}
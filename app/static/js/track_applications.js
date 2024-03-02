document.addEventListener('DOMContentLoaded', (event) => {
    const trackApplicationsForm = document.getElementById('trackApplicationsForm');
    const applicationStatus = document.getElementById('applicationStatus');

    trackApplicationsForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = new FormData(trackApplicationsForm);
        const response = await fetch('/track_applications', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const data = await response.json();
            if (data.message === 'TRACK_APPLICATIONS_SUCCESS') {
                applicationStatus.textContent = 'Application tracking successful!';
                applicationStatus.style.color = 'green';
            } else {
                applicationStatus.textContent = 'Error in tracking applications. Please try again.';
                applicationStatus.style.color = 'red';
            }
        } else {
            applicationStatus.textContent = 'Server error. Please try again later.';
            applicationStatus.style.color = 'red';
        }
    });
});
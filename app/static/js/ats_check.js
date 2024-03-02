document.getElementById('atsCheckForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    let resumeFile = document.getElementById('resumeFile').files[0];
    let formData = new FormData();
    formData.append('file', resumeFile);

    let response = await fetch('/ats_check', {
        method: 'POST',
        body: formData
    });

    if (response.ok) {
        let result = await response.json();
        if (result.message === 'ATS_CHECK_SUCCESS') {
            document.getElementById('atsResult').innerText = 'Your resume has passed the ATS check.';
        } else {
            document.getElementById('atsResult').innerText = 'Your resume did not pass the ATS check. Please review and make necessary changes.';
        }
    } else {
        console.error('Error in ATS check:', response.statusText);
    }
});
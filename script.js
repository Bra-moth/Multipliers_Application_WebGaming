document.addEventListener('DOMContentLoaded', function () {
    const registrationForm = document.getElementById('registration-form');
    registrationForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // Here, you can send the registration data to your server for processing.
        // You can use JavaScript Fetch API or other methods to make an HTTP request to your backend.
        // For example, you can send a POST request with the user's registration data.
        // Example:
        /*
        fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response from the server, e.g., show a success message or handle errors.
        })
        .catch(error => {
            // Handle any errors that occur during the request.
        });
        */
    });
});

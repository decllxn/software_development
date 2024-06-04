document.getElementById("button").onclick = function () {
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    firebase
        .auth()
        .createUserWithEmailAndPassword(email, password)
        .then((userCredential) => {
            // Signed in
            var user = userCredential.user;
            // Optionally, you can update the user's profile with the name
        })
        .then(() => {
            // Redirect to homepage after successful sign up
            window.location.href = "/homepage.html";
        })
        .catch((error) => {
            var errorCode = error.code;
            var errorMessage = error.message;
        });
}


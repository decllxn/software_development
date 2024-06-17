// Html form validation can be done by javascript
// If a form field(fname) is empty, this function alerts a message,
// and returns false, to prevent the form from being submitted
function validateForm() {
    let x = document.forms["myForm"]["fname"].value; // Searches
    // for forms, and inputs with the above names and takes their values
    if (x == "") {
        alert("Name must be filled out");
        return false; // Prevents the form from being submitted
    }
}

// This example finds the form element with id="frm1" in the forms
// collection, and displays all the element values

const x = document.forms["frm1"]; // Finds form element with id="frm1"
let text = "";
for (let i = 0; i < x.length; i++) {
    text += x.elements[i].value + "<br>";
}

document.getElementById("demo").innerHTML = text;
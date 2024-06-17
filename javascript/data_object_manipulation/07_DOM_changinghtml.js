// The easiest way to modify the content of an html element is by using the innerHTML property
// Follows the following syntax
// document.getElementById(id).innerHTML = new HTML

document.getElementById("p1").innerHTML = "New Text!";

const element = document.getElementById("id01"); // Elements inside the document
// with that id are found
// Now replacing the constent

element.innerHTML = "New Heading";

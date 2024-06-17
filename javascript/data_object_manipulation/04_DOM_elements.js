// Often with Javascript, you want to manipulate HTML elements

// Finding element by ID
document.addEventListener("DOMContentLoaded", function() {
    const element = document.getElementById("Intro");
    element.innerHTML = "I found you!";
});

//Finding html elements by tag name
// Thus example finds all <p> elements

const findTag = document.getElementsByTagName("p");
document.getElementById("demo").innerHTML = 
'The text in the first paragraph (index 0) is: ' + findTag[0].innerHTML;

// The example below finds the element with "id=maine"
// and then finds all <p> elements inside "main"
const x = document.getElementById("main");
const y = x.getElementByTagName("p"); // The p's inside
// the main can be accessed using indices starting from 0

// Finding Html elements by class name
// getElementByClassName()
const a = document.getElementsByClassName("intro");
document.getElementById("demo1").innerHTML = 
'The first paragraph (index 0) with class="intro" is: ' + a[0].innerHTML;
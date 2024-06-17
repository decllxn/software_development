// add an event listener that fires when a user clicks a button
document.getElementById("myBtn").addEventListener("click", displayDate);
// define the function that will be called when the button is clicked

function displayDate() {
    document.getElementById("demo").innerHTML = Date();
}

// An addEventListener() method attaches an event handler to the specified element
// addEventListener() method attaches an event handler to an element without overwriting event handlers
// The addEventListener() method is not supported in older versions of Internet Explorer (IE8 and earlier
// The addEventListener() method is supported in all modern browsers, including IE9 and later

// It makes it easier to control how the event reacts
// The JS is seperated from the htm markup, for better readability and allows
// you to add event listeners when you do not control the HTML markup

document.getElementById("myBtn2").addEventListener("click", 
 function() {
    alert("Hello World!");
 }
);

// Adding many event listeners to the same html element
var x = document.getElementById("myBtn3"); // Searches for that element
x.addEventListener("mouseover", myFunction); // links the element, to the event(user action), and then function to be executed
x.addEventListener("click", mySecondFunction);
x.addEventListener("mouseout", myThirdFunction);

function myFunction() {
    document.getElementById("demo2").innerHTML += "Moused over!<br>";
}

function mySecondFunction() {
    document.getElementById("demo2").innerHTML += "Clicked!<br>";
}

function myThirdFunction() {
    document.getElementById("demo2").innerHTML += "Moused out!<br>";
}
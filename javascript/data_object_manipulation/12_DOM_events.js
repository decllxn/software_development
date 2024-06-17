// Html Dom allows Javascript to react to html events
// A js can be executed when an event occurs, like when a user clicks on an HTML
// element.
/**
 * Examples of HTML events:
   - When a user clicks the mouse
   - When a web page has loaded
   - When an image has been loaded
   - When the mouse moves over an element
   - When an input field is changed
   - When an HTML form is submitted
   - When a user strokes a key
 */
 
// You can add on click on almost every element
// A function is called an event handler
function changeText(id) {
    id.innerHTML = "Oooopsss! Not again!";
}

function displayDate() {
    document.getElementById("demo").innerHTML = Date();
}

// Html event attributes
// To assing events to HTML elemenst you can use event attributes
// Example: onclick, onmouseover, onmouseout, onkeydown, onkeyup, onsubmit


// The onload and onunload 
// The onload event occurs when an object has been loaded
// The onunload event occurs when the user leaves the page
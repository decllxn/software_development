// If you want to find all elements that match a specified
// CSS selector(id, class names, types, attributes, values of attributes, etc)
// use querySelectorAll() method

const x = document.querySelectorAll("p.intro");
document.getElementById("demo").innerHTML = 
'The second paragraph (index 1) with class="intro" is: ' + 
x[1].innerHTML;
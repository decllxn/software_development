#!/usr/bin/env node
// Java Script functions are defined using the function keyword
// You can use function declaration or a function exrpession

// Example

function myFunc(a, b) {
    return a * b;
}
console.log(myFunc(3,7));

// Function expressions
// A Js function can also be defined using an expression
// Example

const x = function (a, b) {return a * b}; // Anonymous function
let z = x(5, 8);
console.log(z);
// Functions stored in variables do not need to be invoked
// They are usually invoked using the variable name

// The function constructor()
// Functions can also be defined with a built-in Js function constructor
// called Function()

// Example
const myFunction = new Function("a", "b", "return a * b")
let a = myFunction(4, 8);
console.log(s);
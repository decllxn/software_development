// Variables are used to store data
/*
 Declared using:
 var
 let
 const
*/

// All Javascript variables must be identified with unique names
// The unique names are called identifiers

let a;
const b = 7;

a = 9;
let d = a + b;

console.log(d);

// You can use one statement to declare many variables

let person = "John Doe", carName = "Volvo", price = 200;


// the let keyword

/*
 There are 3 scopes in javascript right now
 Global scope
 Function scope
 Block scope
*/

{
    var x = 2; // var has global scope
    //the contents of var can be accessed even outside the global scope

}


// Redeclaring variables

var x = 10;
// Here x is 10

{
    var x = 2;
    // Here x is 2
}

// Here x is 2


// let and const have block scope
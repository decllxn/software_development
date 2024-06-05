// Variables enables you to commit infomatiorn to the
// memory of a computer

var myName = "Declan";
console.log(myName);

// Var can be changed

myName = "Stacy";
console.log(myName);


function test() {
    var a = "3";
    var b = "8";
    
/***********Do not change the code above 👆*******/
//Write your code on lines 7 - 9:
var z = a;
a = b;
b = z;    
/***********Do not change the code below 👇*******/

    console.log("a is " + a);
    console.log("b is " + b);
}

test()

// variables should follow certain naming schemes
// Give the variables names that follow camelCase format
// do not use keywordsas variable names 
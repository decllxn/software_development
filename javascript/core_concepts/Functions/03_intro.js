// ------Self invoking functions------
// Functions expressions can be made "self-invoking"

// Function expressions will execute automatically if the expression is followed
// by ()


// The function below will call itself
(function () {
    let x = "Hello!";
    console.log(x);
})(); // Parenthesis at the end
// Parenthesis surrounding the function


// ----Functions as values-----
function myFunction(a, b) {
    return a * b;
}
let x = myFunction(4, 3);
console.log(x);

// Functions are objects

// function parameters
// Function parameters are the names lister in the function definition
// Function arguments are the real values passed to and received by the function

// --- Default parameters ---
function myFunction(x, y) {
    if (y === undefined) {
        y = 2;
    }
}
// y is undefined

function myFunc (x, y = 10) {
    return x + y;
} // if y is not defined then y = 10

myFunc(5);


// Js functions have a built-in object called the arguments object

// The argument object contains an array of arguments used when the function was called
// Key word = argument object
// This way you can simply use a function to find (for instance) the highest value in a list of numbers:

x = findMax(1,45,67,32,6,409,45,89); // Converted into an array
// and stored in the arguments object

function findMax() {
    let max = -Infinity;
    for (let i = 0; i < arguments.length; i++) {
        if (arguments[i] > max) {
            max = arguments[i];
        }
    }
    return max;
}

console.log(x);
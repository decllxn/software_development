// The rest parameter (...) allows a function to treat an indefinite number of arguments as an array
// example

function sum(...args) { //args becomes an array
    let sum = 0;
    for (let arg of args) sum += arg;
    return sum;
}

let x = sum (5,78,75,38,28,294,567,53); // All these are now treated as an array
console.log(x);
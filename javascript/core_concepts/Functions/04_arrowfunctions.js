// Arrow functions allows short syntax when writing function
// expressions

let a = function(x, y) {
    return x * y;
}

// Arrow function, doing the same task

const b = (x, y) => x * y;

console.log(a(3, 4));
console.log(b(3, 4));
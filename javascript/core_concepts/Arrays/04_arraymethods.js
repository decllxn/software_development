const fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"];

// Array methods
// unshift();
let a = fruits.unshift("Pineapple"); // Adds an element to the start of an array
console.log(a); // Expected output: 6 (new length of the array)
console.log(fruits); // Expected output: ["Pineapple", "Apple", "Banana", "Cherry", "Date", "Elderberry"]

// push();
let b = fruits.push("Kiwi"); // Adds an element at the back of an array
console.log(b); // Expected output: 7 (new length of the array)
console.log(fruits); // Expected output: ["Pineapple", "Apple", "Banana", "Cherry", "Date", "Elderberry", "Kiwi"]

// pop(); removes an element at the end of an array
fruits.pop();
console.log(fruits);

// shift();
fruits.shift(); // removes element at the fron of the array
console.log(fruits)
// An array is a special variable, which can hold more
// than one value

const cars = ["Saab", "volvo", "BMW"];
const People = [
    "Stacy",
    "Declan",
    "John Doe",
    "Mary Doe"
];


// Accessing arrays using index
console.log(People[0]);

// Using new Keyword to making arrays
const subjects = new Array("English", "Kiswahili", "Biology")

// changing an Array element
subjects[2] = "Physics";
// Biology becomes physics

// An array is an object, there for you can convert it to a string
const fruits = ["Banana", "Orange", "Apple", "Mango"];
console.log(fruits.toString());
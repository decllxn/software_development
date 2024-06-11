// Using Object.values()
// Object.values created an array from property values

const person = {
    name: "John",
    age: 30,
    city: "New York"
};

// create an Array
const myArray = Object.values(person);

// Display the array
document.getElementById("demo2").innerHTML = myArray;
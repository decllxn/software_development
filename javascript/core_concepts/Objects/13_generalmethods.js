#!/usr/bin/env node

// Some general object methods

// Object.assign(target, source)
// Copies properties from a source object to a target object
// Creating an object

const person1 = {
    firstName: "John",
    lastName: "Doe",
    age: 50,
    eyeColor: "blue",
};

// Create Source Object
const person2 = {
    firstName: "Anne",
    lastName: "Smith",
}

// Assign Source to target
Object.assign(person1, person2); // Person 1 gets overriden

//console.log(person1);
//console.log(person2);


// Object.entries()
// Returns an array of key/value pairs in an object

const car = {
    Brand: "Pagani",
    Model: "Utopia",
    Mileage: 20034,
    color: "beige"
}

let text = Object.entries(car);
//console.log(text);
// console.log returns
/*
 [
  [ 'Brand', 'Pagani' ],
  [ 'Model', 'Utopia' ],
  [ 'Mileage', 20034 ],
  [ 'color', 'beige' ]
]
*/
// That's why it becomes easier to loop through the items
// Example

const fruits = {
    Bananas:300,
    Oranges:200,
    Apples:500,
    Guavas:250,
    Melons:450
};

let food = "";
for (let [fruit, value] of Object.entries(fruits)) {
    food += fruit + ": " + value + "\n";
}

console.log(food);

// Objects.entries also can be used to convert objects into maps
const fruitMap = new Map(Object.entries(fruits));
console.log(fruitMap);

// Objects.fromEntires()
// .fromEntries() method creates an object from a list of key/value pairs

const newFruits = [
    ["Apples", 300],
    ["Pears", 900],
    ["bananas", 500]
];

const myObj = Object.fromEntries(newFruits);
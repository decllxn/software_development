#!/usr/bin/env node

// All javascript objects inherit properties and methods from a prototype
function Person(first, last, age, eyecolor) { // This is a constructor function
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eyecolor;
    this.nationality = "English" // default value for object type
    // Every object formed from the above constructor has the default English value
} // We have defined properties for an object type


const myDaughter = new Person("Aura", "lily", 12, "blue");
// Object myDaughter has been created
console.log(myDaughter)
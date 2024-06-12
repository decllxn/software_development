#!/usr/bin/env node
// All Js objects inherit properties from a protoype
// Date objects inherit from = Date.prototype
// Array = array.prototype
// Person = Person.prototype

// The Object.prototype is on e of the prototype inheritance chain
// Using the prototype property allows you to add new propetries
// to object constructors

function Car(Brand, model, mileage, year) {
    this.company = Brand;
    this.model = model;
    this.mileage = mileage;
    this.year = year;
}

Car.prototype.color = "Black"; // Added property to object constructor
const myCar = new Car("BMW", "M5 competition", 32450, 2022);
const dreamCar = new Car("Pagani", "Utopia", 0, 2024)

console.log(myCar);
console.log(dreamCar);

// You can add functions using object.prototype

function Person(name, age) {
    this.name = name;
    this.age = age;
}

// adding new property function using prototype
Person.prototype.greet = function () {
    return `Hello, my name is ${this.name}`
}

// Creating new instance
const person1 = new Person('John', 30);
console.log(person1.greet());
#!/usr/bin/env node
// Introduced in es6
// Javascript classes are templates for objects
// Syntax
// Uses key word class
/*
class className {
    constructor function () {
        ...
    }
}
 */

class Car {
    constructor(name, year) {
        this.name = name;
        this.year = year;
    }
}
// The template for object car can now be created
const myCar1 = new Car("Ford", 2014)
const myCar2 = new Car("Audi", 2016)

// Constructor method is a special method: 
//    - It has to have the exact name "constructor"
//    - It is executed automatically a new object is created
//    - It is used to initialize object properties


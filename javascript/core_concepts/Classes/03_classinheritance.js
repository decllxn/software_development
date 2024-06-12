#!/usr/bin/env node
// To create a class inheritance, use the extend keyword
// A class created with a class inheritance inherits all the methods from another class

// example

class Car {
    consructor(brand) {
        this.carname = brand;
    }
    present() {
        return 'I have a ' + this.carname;
    }
}

class Model extends Car { // Inherits template properties from Car 
    constructor(brand, mod) {
        super(brand);
        this.model = mod;
    }    
    show() {
        return this.present() + ', it is a ' + this.model
    }
}

let myCar = new Model("Ford", "Mustang");
console.log(myCar);
console.log(myCar.show());
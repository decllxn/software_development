#!/usr/bin/env node

// Classes also allow you to use getters and setters
// It can be smart to use getters and setters for properties

class Car {
    constructor(brand) {
        this.carname = brand;
    }
    get cname() {
        return this.carname;
    }
    set cname(x) {
        this.carname = x;
    }
}

// Getters and setters are used if you want to do something special with the valu
// before returning them, or before you set the

const myCar = new Car("Ford");
console.log(myCar.cnam);
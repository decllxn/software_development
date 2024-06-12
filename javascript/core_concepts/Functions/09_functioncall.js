// With the call() method, you can write a method that can be used on different objects

// All functions are methods
// it can be used to invoke (call) a method with the owner as the argument(parameter)
// With call(), an object can use a method belonging to another object

const person = {
    fullName: function() {
        return this.firstName + " " + this.lastName;
    } // Function belonging to the person "Object"
}

const person1 = {
    firstName:"John",
    lastName: "Doe"
}

const person2 = {
    firstName:"Mary",
    lastName:"Doe",
}

// This will return "John Doe"
person.fullName.call(person1);

// This will return "Mary Doe"
person.fullName.call(person2)


// -- Call() Method with Arguments -- 
// call can accept many arguments

const Car = {
    fullCarName: function (mileage, color) { // Taking many arguments 
        return "The " + this.Brand + " " + this.model + " has " + mileage + 
        " on it. And it is color " + color;
    }
} // method in car object
// The method taking arguments, thus we have to call the call() with arguments passed to it
// color and mileage should not be accesse dwith this as they are parameters of the function

// Creating the next object
const myCar = {
    Brand:"Pagani",
    model:"Utopia"
}

let x = Car.fullCarName.call(myCar, 30045, "Beige");
console.log(x);


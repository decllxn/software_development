// The code inside Js will execute when "something" invokes it
// -- Invoking a function as a function -- 
function myFunction (x, b) {
    return x * b;
}
myFunction(10, 2) // will return 20

// -- What is this ---
// this keyword refers to an object
// this refers to different objects dependign on how it is used

// -- GLobal Object --
// When a function is called without an owner object,
// this becomes the global object

// In this example  returns the window object as the value of this

let x = myFunc();

function myFunc() {
    return this;
}
console.log(x);


// -- Invoking a function as a method --
// In JS you can define functions as object methods

const myObj = {
    firstName:"John",
    lastName:"Doe",
    fullName: function () {
        return this.firstName + " " + this.lastName;
    }
}
myObj.fullName();
// will return "John Doe"
// The fullName method is a function
// The function belongs to the object
// myObj is the owner of the function
// THE THING THIS, IS THE OBJECT THAT "OWNS" THE JS CODE
// In this case the value of this is myObj

const Person = {
    fName: "Stacy",
    lname: "June",
    age: 20,
    nameOfPerson: function () {
        return this
    }
}

Person.fullName(); // This will return [object Object] (the owner object)



// -- Invoking a function as a constructor ---
function Car(arg1, arg2) {
    this.brand = arg1;
    this.model = arg2;
}

// This creates a new object
const myCar = new Car("Ford", "GT");

// This will return "Ford"
myCar.brand;

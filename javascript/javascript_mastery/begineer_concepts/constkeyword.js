/*
 const cannot be redeclared
 const cannot be reassigned
 const have block scope
*/

// use const when declaring Arrays, object, FUnction, RegExp

// Const does not define a constant value. It defines a constant reference to a value

// You can create a constant array:
const cars = ["Subaru", "Volvo", "BMW"];

// You can change an element
cars[0] = "Toyota";

// You can add an element
cars.push("Audi")

console.log(cars)


//You You can change the properties of a constant object

// You can create a const object:

const car = {
    type:"Fiat",
    model:"500",
    color:"white"
};

// You can change a property
car.color = "red";

// You can add a property
car.owner = "Johnson";


// const is a block scope 

const x = 10;
//Here x is 10

{
    const x = 2;
    // Here x is 2
}

// Here x is 10
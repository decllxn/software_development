// Functions in objects are called methods
// this keyword is utilized

const person = {
    firstName : "John",
    lastName : "Doe",
    id : 55667,
    fullName : function() {
        return this.firstName + " " + this.lastName
    }
};

console.log(person);
// In js almost everything is an object
/*
 Objects are objects
 maths are objects
 Functions are objects
 Dates, arrays, maps, sets
 */
// Properties can be changed added, deleted and some are read only
const person = {
    firstName : "John",
    lastName : "Doe",
    id : 55667,
    fullName : function() {
        return this.firstName + " " + this.lastName
    }
};

// Accessing object properties
// 1
let lname = person.lastName;

// 2
let id = person["id"];

//3
let fname = person[irstname] 

// Adding properties

person.nationality = "Dutch"

// deleting properties
// using the delete keyword

delete person.lastName
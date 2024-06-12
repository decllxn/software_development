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
// Apply() method, you can write a method that can be used on different objects
// Apply method is similar to call()

const person = {
    fullName: function () {
        return this.firstName + " " + this.lastName
    }
}


const person1 = {
    firstName: "Mary",
    lastName: "Doe"
}

// this will return "Mary Doe"
person.fullName.apply(person1);

// Difference between call() and apply()
// call() takes arguments seperately
// apply() takes arguments as an array

const Huma = {
  fullName: function(city, country) {
    return this.firstName + " " + this.lastName + "," + city + "," + country;
  }
}

const Human1 = {
  firstName:"John",
  lastName: "Doe"
}

person.fullName.apply(person1, ["Oslo", "Norway"]);
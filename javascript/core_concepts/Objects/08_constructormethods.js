// A constructor can also have methods

function Person(first, last, age, eyecolor) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eyecolor;
    this.fullName = function() { // Method
      return this.firstName + " " + this.lastName;
    };
  }

const myMother = ("Lisa", "Monroe", 45, "brown")
console.log(myMother)

// Adding a Method to an object
myMother.changeName = function (name) {
  this.lastName = name;
}


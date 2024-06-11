// Sometimes we need to create many objects of the same type
// tocreate an object type we use an object constructor function
// In other languages the object type is called classes

function person(fist, last, age, eye) {
    this.firstname  = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eye;
    this.nationality = "English" // value has been given, the value is hardcoded and default
}

// In the constructor function, this has no value
// The value of this will becom ethe ne object when a new object is created


// Object type has been made
// Now creatin the objects

const Father = new person("Declan", "Munene", 30, "Black");
const Mother = new person("Stacy", "June", 30, "brown");
const person ={
    name: "John",
    age: 30,
    city: "New York"
};

document.getElementById("demo").innerHTML = person;
// Displaying an object will output
// [object Object]

// Displaying properties
document.getElementById("demo").innerHTML = 
person.name + ", " + person.age + ", " + person.city


// DISPLAYING PROPERTIES IN A LOOP

// Build a text
let text = "";
for (let x in person) {
    text += person[x] + " ";
};

document.getElementById("demo1").innerHTML = text;

// Objects.entries()
// Object.entries makes it simple to use objects in loops

const fruits = {
    Bananas:300,
    Oranges:200,
    Apples:500
};

let text = ""
for (let [fruit, value] of Object.entries(fruits)) {
    text += fruit + ": " + value + "<br>";
}

document.getElementById("demo").innerHTML = text;
const cars = [
    "Pagani",
    "BMW",
    "Audi",
    "Buggatti",
    "Mercedes",
]

let fLen = cars.length;
let text = "<ul>"
for (let i = 0; i < fLen; i++) {
    text += "<li>" + cars[i] + "</li>";
}
text += "</ul>";

document.getElementById("demo").innerHTML = text;
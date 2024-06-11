const fruits = [
    {name:"apples", quantity:300},
    {name:"bananas", quantity:500},
    {name:"oranges", quantity:200},
    {name:"kiwi", quantity:150}
  ];
  
  // Callback function to select low volumes 
function myCallback({ quantity }) {
    return quantity > 200 ? "ok" : "low";
}
  
  // Group by ok and low
const result = Object.groupBy(fruits, myCallback);
  
// Displaying the results
let text = "These fruits are Ok: <br>";
for (let [x,y] of result.ok.entries()) {
    text += y.name + " " + y.quantity + "<br>";
}

text += "<br>These fruits are low: <br>";
for (let [x,y] of result.low.entries()) {
  text += y.name + " " + y.quantity + "<br>";
}

document.getElementById("demo").innerHTML = text;
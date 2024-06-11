// Property values in an object can be other objects

me = {
    myName:"John",
    myAge:30,
    myCar: {
        Name:"BMW",
        model:"M5 cs",
        modelYear:2024,
        mileage:34400
    }
};

// I can access the nested objects using the dot notation or the bracket notation
let myCarBrand = me.myCar.Name;
console.log(myCarBrand);

// Bracket notation
let myCarmileage = me["myCar"]["mileage"];
console.log(myCarmileage);
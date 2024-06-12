const Person = {
    name: "Stacy",
    age: 20,
    herCars: [
        {
            name: "Ford",
            models: [
                "Fiesta",
                "Focus",
                "Mustang"
            ]
        },
        {
            name: "BMW",
            models: [
                "320i",
                "x3",
                "x5"
            ] 
        },
        {
            name: "Fiat",
            models: [
                "500",
                "Panda"
            ]
        }
    ]
}

// To access the arrays inside the arrays, use a for-in loop

for (let i in Person.cars) {
    x += "<h1>" + Person.herCars[i].name + "</h1>";
    for (let j in Person.herCars[i].models) {
        x += Person.herCars[i].models[j];
    }
}
#!/usr/bin/env python3
# Author - Declan Munene
# Date - 18/07/2024
# Description - A script that shows single inheritance without overriding a method


class Car:
    def __init__(self, make, model, year: int):
        self.make = make
        self.model = model
        self.year = year

    def speed(self, speed: int):
        self.speed = speed
        if self.speed > 110:
            return f"This car is moving at {self.speed}, thus it is overspeeding"
        return f"This car is moving at {self.speed}, it is not overspeeding"

class Sedan(Car):
    def __init__(self, make, model, year: int):
        super().__init__(make, model, year) # Inherits attributes

    # Does not override speed
    # Calling it with a return statement, and calling the method
    def speed(self, speed: int):
        return super().speed(speed)

# Creating an instance
myCar = Sedan("Ford", "Mustang", 2022)
print(myCar.speed(90))


class Truck(Car):
    def __init__(self, make, model, year: int):
        super().__init__(make, model, year)

    # Overrides the speed method
    def speed(self, speed: int):
        self.speed = speed
        if self.speed > 65:
            return f"This car is moving at {self.speed}, thus it is overspeeding"
        return f"This car is moving at {self.speed, it is not overspeeding}"

# Creating an Instance
my_dad_car = Truck("Ford", "Ranger", 2021)
print(my_dad_car.speed(70))

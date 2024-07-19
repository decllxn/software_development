#!/usr/bin/env python3
# Author - Declan Munene
# Date - 18/07/2024
# Description - Creating a script that showcases single inheritance with method being
# Overriden


class Car:
    def __init__(self, make, model, year: int):
        self.make = make
        self.model = model
        self.year = year

    def vehicle_newness(self):
        if self.year > 2020:
            return f"This car was made in {self.year}. This is new"
        return f"This car was made in {self.year}. This is old"

class Sedan(Car):
    def vehicle_newness(self):
        if self.year > 2021:
            return f"This car was made in {self.year}. This is new"
        return f"This car was made in {self.year}. This is old"

# Usage
myCar = Sedan("BMW", "M3 competition", 2020)
print(myCar.vehicle_newness())

# This is a more advanced example showcasing single inheritance
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def honk(self):
        print(f"{self.make} {self.model} is honking.")

# Example Usage
my_car = Car("Toyota", "Corolla", 4)
my_car.start() # Inherited method
my_car.honk() # local method
my_car.stop() # inherited method

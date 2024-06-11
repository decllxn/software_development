# polymorphism is often used in Class methods, where we can have
# multiple classes with the same method name

# Example

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self): # First form of the move method
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self): # second form of move
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
 
    def move(self): # third form of move
        print("Fly!")

car1 = Car("Ford", "Mustang")       # Create a car class
boat1 = Boat("Ibiza", "Touring 20") # Create a Boat class
plane1 = Plane("Boeing", "747")     # Create a Plane class

for x in (car1, boat1, plane1):
    x.move()

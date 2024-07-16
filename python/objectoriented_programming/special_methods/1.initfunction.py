# The init function is a special method in Python
# It is called when an object is created
# It is used to initialize the object's attributes
# It is called automatically when the object is created
# It is used to set the initial state of the object
# The primary purpose of the __init__ function is to initialize
# the instance attributes of the class

class Car:
    def __init__(self, make, model, year: int):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

# Creating an instance of a Car(An object now)
car1 = Car("Ford", "Mustang", 2022)

# Accessing the attributes
print(car1.model)
print(car1.make)
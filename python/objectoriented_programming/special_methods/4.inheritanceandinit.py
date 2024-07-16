# When creating a subclass, you can override the init method.
# To ensure that the base classes's init method is called, use super()

class Vehicle:
    def __init__ (self, type, model):
        self.type = type
        self.model = model
    
class sedan(Vehicle): # This is a sub-class of vehicle
    def __init__(self, type, model, color):
        super().__init__(type, model) # This calls the init method of the parent class
        self.color = color
        # inherits attributes from the parent class

# can add new attributes to the sub-class
myCar = sedan("sedan", "BMW", "black")
print(myCar.type)
print(myCar.color)
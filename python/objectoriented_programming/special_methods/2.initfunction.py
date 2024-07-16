# The self-parameter: Is a reference to the current instance of the class
# The self-parameter is used to access the attributes and methods of the class
# Every method in a class must have 'self' as it's first parameter
# The self-parameter is not passed when calling a method
# The self-parameter is automatically passed by the interpreter when calling a method

# You can provide default values in the init function

class House:
    def __init__(self,
                 address: str,
                 num_bedrooms: int,
                 num_bathrooms: int,
                 area: int,
                 color: str = "White", # Default value
                 hasCompound: bool = True # Default value
                 ):
        self.address = address
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.area = area
        self.is_furnished = False
        self.color = color
        self.hasCompound = hasCompound

House1 = House("Mungai Drv", 5, 6, 200)
# Accessing the attributes

print(House1.num_bathrooms) # Attribute passed
print(House1.color) # Attribute given a default value in the param
print(House1.is_furnished) # Attribute given value when it was accessed
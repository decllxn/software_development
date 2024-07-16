# Using the init function for validation
# You can add validation logic within the init function to ensure
# The instance is created with the valid attributes

class Laptop:
    def __init__(self, brand, model, price):
        if not isinstance(brand, str):
            raise ValueError("Brand must be a string")
        if not isinstance(model, str):
            raise ValueError("model must be a string")
        if not isinstance(price, int):
            raise ValueError("price must be an integer")
        if price < 0:
            raise ValueError("price must be a positive integer")
        self.brand = brand
        self.model = model
        self.price = price

myLaptop = Laptop("lenovo", "legion 5", 4000) # This instance(object) does not raise an error
herLaptop = Laptop ("lenovo", "strix", -344) # This raises an error in price

print(myLaptop.brand)
print(herLaptop.price) # An error occurs
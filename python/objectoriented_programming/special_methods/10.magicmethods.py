# Magic methods are special methods in python that start and end
# with double underscores. They are used to override the default
# behavior of a class or object.
# Also known as dunder methods
# They allow you to define specific behaviours for your objects
# and classes, in various contexts 
# example
#__str__ and __repr__

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__ (self): # Executes a print statement 
        return f"Name: {self.name}, Age: {self.age}"
    # __repr__
    def __repr__(self): # Executes a print statement
        return f"Person(name='{self.name}', age={self.age})"
        # Allows you to put ticks in your print statement

mygirl = Person ("Alice", 30)
print(mygirl)
print(repr(mygirl))

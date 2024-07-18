from typing import Any


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # getattr is called when accessing an attribute that doesn't exist in the
    # objects dictionary
    def __getattr__(self, attr):
        return f"{attr} attribute not found"
    
    # Handles setting attributes, modifying the internal dictionary
    # directly
    def __setattr__(self, name, value):
        self.__dict__[name] = value
   
    # Handles deleting the attributes from the object's dictionary
    def __delattr__(self, name):
        del self.__dict__[name]

    # returns a list of valid attributes for the object, used by the
    # dir() function
    def __dir__(self):
        return ['name', 'age']
    
# Example usage

mygirl = Person ("Stacy June", 20)
print(mygirl.height) # getattr, searched for it and never found the
# attribute, so it returned the default message
# prevents python3 from returning an error message

mygirl.height = 156
print(mygirl.height) # __setattr__ was called, it modified the dictionary

del mygirl.height
print(mygirl.height) # __delattr__ was called, it deleted the attribute
print(dir(mygirl))
   
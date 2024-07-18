#!/usr/bin/env python3

# Single inheritance is a fundamental concept in object-oriented programming
# Where, a class(child or subclass) inherits one other class(Parent or superclass)
# This allows the child class to inherit the attributes and methos of the parent class, promoting code reusability and organization

## Example

class Parent:
  def __init__(self, name):
    self.name = name
    
  def greet(self):
    print(f"Hello, my name is {self.name}")
    
 class Child(Parent):
   def __init__(self, name, age):
     super().__init__(name)
     self.age = age
     
   def display_age(self):
     print(f"I am {self.age} years old")
     

child = Child("Alice", 10)
child.greet() # Output: Hello, my name is Alice
child.display_age() # Output: I am 10 years old

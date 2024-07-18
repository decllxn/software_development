#!/usr/bin/env python3
# Destructors are methods that are called when an object is about to be destroyed
# Destructors are called automatically when the object is destroyed
# they perform the necessary clean up, such as:
  # releasing external resources
  # closing files
  # Or other tasks

# Example

class Person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} has been created.")
    
    def __del__(self):
        print(f"{self.name} has been destroyed.")
    
# Creating an instance
myfriend = Person("Stacy June")

del myfriend

# Output:
# Stacy June has been created.
# Stacy June is being destroyed
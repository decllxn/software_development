#!/usr/bin/env python3
# practice questions 1

# Single Inheritance Instruction:

# Create a base class Shape with a method calculate_area().
# Create a subclass Rectangle that inherits from Shape and overrides calculate_area()
# to calculate the area of a rectangle.

class Shape:
    def calculate_area(self):
        pass # Method is to be overidden by child class

class Rectangle(Shape):
    def __init__(self, length, width):
        self.width = width
        self.length = length

    # Method overriden in child subclass
    # Self is passed as an argument, so that the method can access
    # All attributes in the dictionary of the class
    def calculate_area(self):
        return self.width * self.length

## Example usage
class_room_floor = Rectangle(5, 10)
print(f"Area of the rectangle: {class_room_floor.calculate_area()}")

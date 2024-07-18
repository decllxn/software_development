# init method is a constructor
# it is a special method used when you create an object of a class
# Classes are like blue prints for creating objects


class Point: # Definition of a class, using the class keyword
    def __init__ (self, x, y): # Initializes the object with initial values for it's attributes
        self.x = x
        self.y = y

# Create a point instance (The object itself)
# You can create amany objects from one class

myPoint = Point(3, 5)
print(f"Point co-ordinates: ({myPoint.x}, {myPoint.y})")


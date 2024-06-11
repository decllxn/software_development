# Inheritance allows us to define a class that 
# inherits all the methods and properties from another class

# Parentclass, the class being inherited from
# The following class has first name, last name and a print name method

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Using the person class to create an object, and then execute the printname method:

human1 = Person("John", "Doe")
human1.printname()

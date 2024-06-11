from parentclass import Person

# This will be my child class
# Child class is the class that inherits from another class, also called derived class

class Student(Person):
    pass # Allows you to bypass arguments that are to be passed


# You can use the student class to create an object and execute the method

x = Student("Mike", "Olsen")
x.printname() # Outputs John Doe, and Mike Olsen

# using the import statement, it shows that objects too can be imported



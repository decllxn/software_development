# Python is an object oriented programming language

# A class is like an object constructor, a "blueprint" for creating objects
# keyword class

class my_class:
    x = 5

# Above is a simple class

# printing the values of my class above
p1 = my_class() # The class and it's contents have been assigned to p1
print(p1.x)

# __init__() function
# it is a built-in function

# All classes have an __init__() function and are always executed
# when the class is being initiated
# the __init__() functions is to assign values to objects properties, or other operations that are necessary to do when the object is being created

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person_one = Person("John", 36)

print(person_one.name)
print(person_one.age)

# the init() function is called automatically every time the class is being used
# to create a new object


# __str__() function
# controls what should be returned when the class object is represented as a string

# The string representation of an object WITH the __str()__ function 

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} \n{self.age}"
    
human_one = Human("Declan", 20)

print(human_one)
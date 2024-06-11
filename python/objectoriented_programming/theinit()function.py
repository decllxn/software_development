from parentclass import Person

# The __init__() function is called automatically everytime the class is
# being used to create a new object

# when you add another innit functions, the child will no longer inherit the parent's innit function
# the new innit function override s the other one

class Student(Person): # The person class passed as a parameter
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname) # Added the parent's innit as a property
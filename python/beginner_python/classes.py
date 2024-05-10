# Used to make data more organized
# Used to work with data
# There's data you cannot represent as strings, numbers or boolean
# In python, you can create your own data types
# like a phone data type - example
# in class you define your own data type

# creating student class

class student:
    # the function below in this case helps you map out attributes of a student
    def __init__(self, name, major, gpa, is_on_probation): #initialized function
        self.name = name
        self.major= major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

# in this case an object is an actual student
# class is an overview of student data type

def on_honor_roll(self):
    if self.gpa >= 3.5:
        return True
    else :
        return False

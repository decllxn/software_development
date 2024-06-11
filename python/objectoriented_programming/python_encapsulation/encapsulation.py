# Encapsulation refers to the wrapping of data under a single unit
# Protective sheild that protects data from being accessed by code outside the sheild


# Encapsulation advantages
# Data hiding
# Flexing
# Reusability

# example

class Edureka():
    def __init__(self):
        self.course = "python progamming course"
        self.__tech = "python" # adding the __ before tech hides it
        # __tech becomes a private variable

    def CourseName(self):
        return self.course + self.__tech
    
ob = Edureka()

print(ob.course)
print(ob._Edureka__tech) # Adding _ before class name enables you to access the hidden attributes
print(ob.CourseName())

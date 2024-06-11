class Edureka():
    def __init__(self):
        self.course = "python progamming course"
        self.__tech = "python" # adding the __ before tech hides it
        # __tech becomes a private variable

    def CourseName(self):
        return self.course + self.__tech
    
    def get__tech(self): # the getter function
        return self._tech
    
    def set_tech(self, t): # setter function
        self.__tech == t
    
ob = Edureka()

ob.set__tech("Machine Learning") # Calling the setter function
ob.get__tech() # calling the get functions

print(ob.course)
print(ob._Edureka__tech) # Adding _ before class name enables you to access the hidden attributes
print(ob.CourseName())
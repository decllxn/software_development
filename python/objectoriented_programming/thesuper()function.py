from parentclass import Person

# Python also has a super() function that will make the child class inherit all the methods and properties

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year # year added as a property

        # adding a method

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


# NB: if you add a method in the chld class with the same name as the function in the parenr class,
#     the inheritance of the paren tmethod will be overriden

person_1 = Student("Declan", "Munene", "2023")
person_2 = Student("Stacy", "June", "2014")

print(person_1.firstname)
print(person_2.lastname)

# You can add properties and methods to the child class


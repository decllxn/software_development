from classes import student

#This is the object file
#We are importing the defined data type (class) in the other file
student1 = student("Jim", "Engineering", 4.0, False)
student2 = student("Stacy", "Computer", 4.3, True)

#Object is an instance of a class
print(student1.name) # Prints out student name

#when you pass in the parameters the init function comes into play
#When you create a student you are calling the __init__ function

# The del statement is a python destructor
# the del statement is used to delete objects
# del statement is used to delete a variable
# del statement is used to delete a list
# del statement is used to delete a dictionary
# del statement is used to delete a tuple
# del statement is used to delete a set

# Example
x = 10
del x
# Now, x is no longer defined
print(x) # NameError: name 'x' is not defined

list = [1, 2, 3, 4]
del list[2]
# Now, list is [1, 2, 4]

dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

del dictionary['c'] # Deleting a dictionary entry
print(dictionary)
# {'a': 1, 'b': 2, 'd': 4} Output

class MyClass:
    def __init__(self):
        self.x = 10
    
obj = MyClass()
del obj.x

# Now, obj.x is no longer defined
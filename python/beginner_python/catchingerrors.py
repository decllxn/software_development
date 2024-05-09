#Errors stop programs from running
#we can handle errors in python and preventing code from from breaking

number = int(input("Enter a number: "))
print(number)
# When you enter a string, there's an error
#There's a way to handle errors
#Because you don't want the error because of the user

#We use the try and except block
#try except block

try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError: #specifying type of error to look for
    print("Invalid input")

#When user inserts string in the  above program Invalid input is outputed and program does not return error message


try: 
    value = 10 / 0 #Nothing like 10 / 0 in math
    print(value)
except ZeroDivisionError as err: #as stores in to a variable
    print(err)
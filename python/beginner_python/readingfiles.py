# Using python to read files outside this file
# I will be reading employees.txt

employee_file = open("employees.txt", "r")# Opening the file you want to open
#Contents of file stored in variable
#when you open the file you need to close it

employee_file.close() #note extension is used on the variable

#modes
# "a" you can append info to end
# "r" read file
# "r+" read and write file
# "w" write file


#How to get information on a file
#you can print out contents print()

#checking if file is readable = readable

print(employee_file.readable()) # returns boolean

print(employee_file.read())

#readline reads the first line then goes on
print(employee_file.readline()) #reads first line
print(employee_file.readline()) #reads second line

#readlines() takes content and stores them in array/list
print(employee_file.readlines())
#You can use readlines with for loops
for employee in employee_file.readlines():
    print(employee) #Prints out each line
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
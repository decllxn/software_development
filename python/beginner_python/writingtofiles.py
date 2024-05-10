# I have to comment out the code so that on rerun it doesn't mess up the list
employee_file = open("employees.txt", "w") 
#employee_file.write("\nKelly - Customer Service")
#Appends a line to the end of the file
#If you run file again it'll append again

employee_file.close()

# using "w" will overwrite existing file


employee_file1 = open("employees1.txt", "w") # creates a new file

employee_file1.write("Stacy June - CEO")
employee_file1.close()

# You can right out a web page using python

web_page = open ("index.html", "w")
web_page.write("<!DOCTYPE html>")

web_page.close()

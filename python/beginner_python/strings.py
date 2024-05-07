# Quotation marks for strings
print ("Girrafe Academy")

#\n for new line

print ("Girrafe\nAcademy")

#\ escape character

# string variable

phrase = "Giraffe Academy" # use quotation marks

# Concatenation
# Process of taking a string and storing another string onto it

print (phrase + " is cool")

#functions
#block of code that executes task

#.lower() makes string lower case
#.upper() makes string upper case
#.islower() checks if string is all in lower case
  # it is a boolean expression
print(phrase.lower())

#length of string len(string)

print(len(phrase))

#grabbing character of string
print(phrase[0])

#adding [] and index inside of it
#indexing starts from zero

#index function = where character is in the string
#string.index("character") returns index of the character
#"character" the parameter of the function

print(phrase.index("G"))

#replace function

print(phrase.replace("Giraffe", "Elephant"))


#output is now Elephant academy instead of Giraffe academy
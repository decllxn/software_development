# module - python file that we can import to our current python file
# say we have a file with useful variables and 
# I will be using the file "usefultools.py"

#What if you need to use the functions of the other files?

import usefultools #You can access like this
#When importing do not write the extension of the file

print(usefultools.roll_dice(10)) # takes function from other file

#pip is a program used to install python modules
#It's a package manager like npm
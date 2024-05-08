#Word names the dictionary
#Value defines the dictionary

#giving the dictionary a name
#use calibrackets {}
#Inside calibrackets {key:value}
#Keys could also be numbers
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])
#You refer the key and the value of the key is returned 

#You can use the get() function also

print(monthConversions.get("Dec"))

#Using the get() function also allows you to pass another argument in case the key is not there

print(monthConversions.get("Luv", "Not a valid key"))
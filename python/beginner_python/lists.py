#Lists help in handling large data types
#Give the name of the lists descriptive names
#Use square brackets

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

#You can access the individual values independently
# You can store numbers, strings, boolean

print(friends) # prints whole list 

# you can refer each element with an index
# indexing starts at 0

print(friends[0]) # "Kevin"
print(friends[2]) # "Jim"


#You can also use negative numbers for indexing
#-1 starts list from the last element
print(friends[-1]) # "Jim"

print(friends[1:3]) # grabs elements 1 upto 3 but excludes 3 
# gives "Karen and "Jim"

print(friends[1:]) # grabs 1 and everything after it

# elements are mutable
friends[1] = "Mike" #changes "Kevin" to "Mike"
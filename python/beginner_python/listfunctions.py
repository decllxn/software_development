lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

# learning most common functions
# print() prints out entire list

#extend() appends a list to another list
#friends.extend(lucky_numbers)

#append() adds element to end of the list
friends.append("Declan")
print(friends)
#insert() takes element and puts it at any position in list
# Takes two arguments, index position and element to be added

friends.insert(1, "Kelly")
print(friends)
#remove() removes specific element

friends.remove("Kelly")
print(friends)

#clear() removes everything in the list
#pop() removes last element in the list

#checking if an element is in the list
print(friends.index("Karen"))

#count() shows how many times an element has been repeated in the list
print(friends.count("Jim")) #returns 2

#sort() alphabetical order and numerical order, ascending order
#reverse() descending order
#copy() copies list onto another list

friends2 = friends.copy()
print(friends2)

#Special type of loop
#Allows you to loop through a collection of items

#for....in loop
#Looping through string
for letter in "Giraffe Academy":
    print(letter)

#You can use this for looping through arrays(lists)

friends = ["Declan", "Stacy", "June", "Munene"]
for name in friends:
    print(name)

#Looping through series of numbers 
for index in range(10):
    print(index)

#range() does not include the last number

len(friends) #gives number of elements in array

#Since range() function does not go upto the last number
#it's perfect for looping through array indices
#As they start from 0
for index1 in range(len(friends)):
    print(index1)

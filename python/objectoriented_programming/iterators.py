# An iterator is an object that contains a countable number of values
# an iterator is an object that can be iterated upon

# Typically, an iterator is an object which implements the iterator protocol,
# which consists of __iter__() __next__()

# lists, tuples, dictionaries and sets are all iterable objects
# They are iterable containers which you can get an iterator from

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
next(myit)
print(next(myit))

# Strings are also iterable objects

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
next(myit)
next(myit)
next(myit)
print(next(myit))

# looping through an iterator

for x in mytuple:
    print(x)

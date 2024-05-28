# Many programs are written to automate repetitive tasks that are better suited to machines
# In python, the most common way to organize this kind of work is by using a sequence of values stored in list type
# Dictionary, stores keys mapped to corresponding values
# Dictionaries deal with book keeping
# Dictionary is also called an assortive array or a hash table


## Slicing
# slicing allows you to access a subset of sequences's items with minimal effort
# built-in types for slicing  LIST, STR, BYTES
# slicing can be extended to any python class that implements the __getitem__
# and __setitem__ special methods
# syntax for slicing = (somelist[start:end])

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'
     'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
     ]
print('Middle two: ', a[3:5])

print('All but ends: ',a[1:7])

# in [start:end] start is inclusive but end is exclusive

print(a[2:6])

# When slicing from the start of a list leave out zero to reduce visual noise
# assert a[:5] == a[0:5]
# assert a[5:] == a[5:len(a)]

print(a[:]) # prints all the list
print(a[:5]) # prints indices 0 - 4

print(a[:-1]) # subtracts one from the end
print(a[-3:-1]) # starts from the 3rd last item and one from the end

# Different ways of using 20 in list

first_twenty_items = a[:20]
last_twenty_items = a [-20:]

a[20] #accesses the item with the 20th index

# results of slicing is a whole new list

b = a[3:]
print(b)

b[1] = 'abc' #replaced index 1 with 'abc' in list b, list a remains unaffected
print(b)
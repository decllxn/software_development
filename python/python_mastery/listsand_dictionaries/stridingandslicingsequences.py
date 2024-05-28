# syntax is 
#  some_list[start:end:stride]

from lists_modules import random_numbers 

#the stride lets you take for example the odd nth items
odds = random_numbers[::2] #starts from index 0 and jumps one position
print(odds)

evens = random_numbers[1::2]
print(evens)

#often the stride behaviour can introduce bugs
#python trick forreversing a byte string is to slice the string with a stride of -1;

x = b'mongoose'

y = x[::-1]
print(y)

#negative striding
x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x[::2] # select every second item starting from the beginning
x[::-2] # jump on item starting from the back

a = x[-2::-2] # a prints ['g', 'e', 'c', 'a']
b = x[-2:2:-2] # b prints ['g', 'e']
c = x[2:2-2] # c prints nothing

#striding and can be extremely confusing, if it's a must you use it together
#try using one assignment and then another one for striding

y = x[::2]
z = y[1:-1]
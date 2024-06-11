# to create an object as an iterator you have
# to implement the methods __iter__()
# and __next__()

# __init__ () for initializing objects
# __iter__() for initializing, but must also return the iterator object itself

# __next__() allows you to do operations, and must return the next item in the sequence

# Example

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self # must return the iterator object
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyNumbers()
myiter = iter(myclass)




# create an even number iteration

class evenNumbers:
    def __iter__(self):
        self.b = 2
        return self
    
    def __next__(self):
        x = self.b
        self.b += 2
        return x
    

printNums = evenNumbers()
number_sequence = iter(printNums)

print(next(number_sequence))
print(next(number_sequence))
print(next(number_sequence))
print(next(number_sequence))
    
# to prevent iteration from going on forever
# We use the StopIteration statement

class myoddNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration # prevents continous looping
        
oddnums = myoddNumbers()
my_iteraion = iter(oddnums)

for x in my_iteraion:
    print(x)
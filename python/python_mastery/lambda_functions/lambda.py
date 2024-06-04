# A lambda functions is a small anonymous function.
# A lambda function can take up any number of arguments, but can only have one expression

x = lambda a : a + 10
print(x(5))

# can take up any number of arguments

y = lambda a, b : a * b
print(y(5, 7))

# lambda is better shown when you use them as an anonymous function inside a function

def my_function(n):
    return lambda a : a * n

myAnswer = my_function(2)
print(myAnswer(11))

# A function that triples

mytripler = my_function(3)
print(mytripler(11))
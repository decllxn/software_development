# Makes programs alot smarter

# creating boolean variable
 
is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
elif is_male and not(is_tall):
    print ("You're a male and you are tall")
else:
    print("You are a female or short")

#you can put as many variables as possible in the if statements
#or operator (or)
#and operator (and)
#elif conditions:

def max_num(num1, num2, num3)
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num3
    else:
        return num3

print(max_num(300, 40, 5))
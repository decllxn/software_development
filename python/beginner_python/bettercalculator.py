num1 = float(input("Enter first number: "))
op1 = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op1 == "+":
    print(num1 + num2)
elif op1 == "-":
    print(num1 - num2)
elif op1 == "/":
    print(num1 / num2)
elif op1 == "*":
    print(num1 * num2)
else:
    print("Invalid operator")

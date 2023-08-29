# Checking the python version
import os

print("Hello World from ")
os.system("python --version")

# Match case in python is justlike switch statement in java and c++
x = int(input("Enter the number"))

match x:
    case 1:
        print("value = 1")  # no neet to use break
    case 2:
        print("value = 2")
    case 3:
        print("value = 3")
    case 4:
        print("value = 4")
    case _ if x != 90:  # Default case
        print(x, " not 90")  # we can give multiple default cases using if elsif and else
    case _ if x != 80:
        print(x, " not 80")
    case _:
        print(x)

# ------Practice-------
x = int(input("Enter the first number"))
op = str(input("Enter the operation  e.g. +, -, *, / = "))
y = int(input("Enter the second number"))

match op:
    case '+':
        print("Sum = ",(x + y))
    case '-':
       print("Subtraction = ", (x - y))
    case '*':
        print("Multiplication = ", (x * y))
    case '/':
        print("Division = ", (x / y))
    case _:
        print("Invalid operation...")

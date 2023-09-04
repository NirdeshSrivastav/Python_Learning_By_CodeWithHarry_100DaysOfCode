a = int(input("Enter your age = "))
print("Your age is = ", a)

# Conditional operator
# >, <, >=, <=, ==, !=
print(a > 18)
print(a <= 18)
print(a == 18)
print(a != 18)

if (a > 18):
    print("you can drive")
else:
    print("you can't drive")
print("end")

# -----ex 1------
applePrice = 50
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1kg apple to the cart")
else:
    print("Alexa, do not add apples to the cart")

# elif statement
if (budget - applePrice > 50):
    print("Alexa, add 1kg apple to the cart")
elif applePrice - budget > 70:
    print("it's ok you can add apples")
else:
    print("Alexa, do not add apples to the cart")

# -----ex 2------
num = int(input("Enter the value of num = "))

if num < 0:
    print("Number is negative")
elif num == 0:
    print("Number is Zero")
else:
    print("Number is Positive")

# Factorial 3 = 3 * 2 * 1
# Factorial 2 = 2 * 1
# Factorial 1 = 1
# Factorial 0 = 1

def fibonacci(n):
    """It takes a number and produces the fibonacci"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * (factorial(n - 1))


# number = int(input("Enter the number to find out the factorial = "))
# print(factorial(number))

for i in range(5):
    print(fibonacci(i))
print(fibonacci.__doc__)

# Function definition
def gmen(a, b):
    mean = (a * b) / (a + b)
    print(mean)


def great(a, b):
    if a > b:
        print("A is greater")
    else:
        print("B is greater")


# driver code
a = 9
b = 8
gmen(a, b)  # Function call
great(a, b)


# if you want declare the function and want to define it ater then you can write pass into the function
def isLesser(a, b):
    pass

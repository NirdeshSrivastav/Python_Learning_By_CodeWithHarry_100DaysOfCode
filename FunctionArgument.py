# required argument
def average(a, b):
    print("The average is  = ", (a+b)/2)


# Default Argument
def sum(a=1, b=9):
    print("Sum  = ",(a+b))


#mix default and required
def greet(fname,mname = "agrawal", lname = "whatson"):
    print("Hello,", fname,mname,lname)


# Will take number as tuple and return the values
def averagsum(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("average  ",sum/len(numbers))
    return sum/len(numbers)


# will take the arguments as dictionary
def name(**name):
    print("Name  = ", name["fname"], name["mname"],name["lname"])


name(fname = "safal", mname= "kumar", lname= "srivastav")
avg = averagsum(5, 6, 7, 1)
print(avg, "\t", type(avg))

average(4, 6)
sum()  # Funtion will be called without arguments
sum(3, 5)  # Funtion will ignore defaults and replace with 3, 5
sum(a=5)

greet("Eric")
greet("Ramesh","kumar")
greet("Ramesh","kumar","jain")
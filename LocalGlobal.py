x = 4  # this is a global variable
print(x)

def hello():
    global x
    x = 10  # it will change the global variable x
    y = 5  # local variable
    print(f"The local y is {x}")
    print("Hello Harry")


hello()
print(f"The global x is {x}")



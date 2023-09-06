# Set can contain duplicate values but prints only unique values
s = {2, 4, 2, 6}
print(s)

# it does not maintain any insertion order
info = {"Carla", 19, False, 5.9, 19}
print(info)

# if we use this syntax then the type will be dictionary
harry = {}
print(type(harry))

# so to make empty set write this
harry = set()
print(type(harry))

# to access the values of the set
for value in info:
    print(value)

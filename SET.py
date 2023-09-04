# Operation On lst data type

# Create a set
set1 = {1, 2, 3, 4, 5}
print(set1)

# to check the addressnof variable
print(id(set1))

# If we add duplicate data in the set it automatically eliminates all the duplicate data
char = {1, 2, 3, 4, 3, 2, 4, 5, 6}
print(char)

char = {'aa', 'bb', 'cc'}
print(char)

char = {'apple'}
print(char)

char = {'a', 'p', 'p', 'l', 'e'}
print(char)

char = {'a', 'p', 'p', 'l', 'e'}
print(char)

# we can create a set object
colourS = set()
# Adding data in set
colourS.add("red")
colourS.add("pink")
colourS.add("yellow")
print(colourS)

fruits = set()
fruits.update([1, 2, 3, 4])
fruits.update(["safal"])
# fruits.add(9,8) Error add takes only one argument
print(fruits)

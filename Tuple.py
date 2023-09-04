tup = (1, 5, 6, "sfal")
print(tup)
print(type(tup))

# we can't change tuples
# tup[0] = 1

# tup2 = (1)  # if you write one element like this then it will be treated as int
tup2 = (1,)
print(type(tup2))

# tuples are iterable
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

# to check the element is exists in thje tuple or not
if 5 in tup:
    print("Number exists")
else:
    print("Number does not exists")

# if we want to do slicing then after slicing a ntuple is returnd
# slicing is just like lists
tup2 = tup[1:4]
print(tup2)

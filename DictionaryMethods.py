ep1 = {
    122: 45,
    123: 89,
    567: 69,
    670: 69
}
ep2 = {
    222: 67,
    566: 98
}

ep1.update(ep2)
print(ep1)

# to clear a dictionary totally
ep1.clear()
print(ep1)

# to create an empty dictionary
empty = {}
print(empty)

# to delete a key-value pair from dictionary
ep1.pop(122)
print(ep1)

# to delete last key-value pair from dictionary
ep1.popitem()
print(ep1)

# to delete only one item from a dictionary
del ep1[122]
print(ep1)

# to delete whole dictionary
del ep1
print(ep1)

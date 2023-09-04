l = [6, 2, 3, 4]
print(l)

# to add an element at last of the list
l.append(5)
print(l)

# to sort the list
l.sort()
print(l)

# to sort in decreasing order
l.sort(reverse=True)
print(l)

# to reverse the original list
l.reverse()
print(l)

print(l.index(2))  # returns the index of the argument

print(l.count(2))  # returns the number of how many times an element exists in the list

m = l
m[0] = 5  # --| both l and m pointing at the same memory location that's why if we make any change in the m it will change the l automatically.
print(l)  # --| both l and m pointing at the same memory location that's why if we make any change in the m it will change the l automatically.

# if you want to make a fresh list with the values of another list.
a = l.copy()
a[0] = 10
print(l)
print(a)

# to update a value on given index
l.insert(1, 899)
print(l)

# to add another list in a list's end point
m = [900, 1000, 1100]
l.extend(m)
print(l)
# to concatenate two list and store into another list
k = l + m
print(k)

s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
# to combine two sets uniquely
print(s1.union(s2))  # this will generate a new set

# to update a set
s1.update(s2)  # ADDS values of the s2 list into the s1 list
print(s1)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)

cities.update(cities2)
print(cities3)

# intersection method
cities3 = cities.intersection(cities2)  # returns common values in both the sets
print(cities3)

cities.intersection_update(cities2)
print(cities)

# symmetric difference
cities3 = cities.symmetric_difference(cities2)  # returns the un-common items from both the lists
print(cities3)
# difference
cities3 = cities.difference(cities2)  # returns the list1 - list2 items
print(cities3)

# to check whether the lists do not have any common elements.1
cities = {"Kathmandu", "Islamabad", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.isdisjoint(cities2)  # returns boolean
print(cities3)

# to check whether the list1 is the superset of list2.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Madrid"}
cities3 = cities.issuperset(cities2)
print(cities3)

# to add new elements into a set
l1 = {1, 2, 3, 4}
l1.add(5)
print(l1)

# to add more than 1 element into a set
l1 = {1, 2, 3, 4}
l1.update("safal", "saksham")
print(l1)

# to remove element from a set
l1 = {1, 2, 3, 4}
l1.remove(2)  # if the element is not exists in the list then it raise an error.
# l1.remove(7)  # it will raise an error.
print(l1)

# to descard element from a set
l1 = {"safal", "Saksham", "hritik"}
l1.discard("rishu")   # if the element is not exists in the list then it does not raise any error.
print(l1)

# to remove the last element of the set.
l1 = {"safal", "Saksham", "hritik"}
s = l1.pop()
print(l1)
print(s)

# to clear all the elements from the set
l1 = {"safal", "Saksham", "hritik"}
if "safal" in l1:
    print("Value Exists")

# to delete the set
l1 = {"safal", "Saksham", "hritik"}
del l1
print(l1)  # will throw an error because we've deleted the l1 variable

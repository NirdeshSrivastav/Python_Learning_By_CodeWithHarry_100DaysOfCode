# Tuples can not be changed....
# if you want to make change in tuple then you must have to copy the tuple and then perform any change operation.
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

# if we want to concatenate two tuples then we don't need to convert tuple into list.
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

# to check the occurences of the element into a tuple
tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple1.count(3)
print("Count of 3 in the tuple  is = ", res)

# index function
res = tuple1.index(3)  # will rise a valueerror if element does not exists.
print(res)

# index function to check into a specific index bound
res = tuple1.index(3, 4, 8)
print(res)

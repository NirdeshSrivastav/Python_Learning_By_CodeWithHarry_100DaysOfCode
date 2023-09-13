dic = {
    "Name": "Safal",
    "Class": "BCA",
    "Language": "JAVA"
}
print(dic["Name"])

empID = {
    101: "Sudarshan",
    102: "Nirdesh",
    103: "Mohit"
}

print(empID[103])
print(empID)

# method to get the elements from dictionary
info = {'name': 'Kiran', 'age': 19, 'eligible': True}
print(info)  # will print all the elements from the dictionary
print(info.get('name2'))  # will not throw any error even if the key does not exist in the dictionaries
# print(info['name2'])  # will throw a key error if the key does not exist in the dictionaries

# to get all the keys from the dictionaries
print(info.keys())

# to get all the values from the dictionaries
print(f"The values of the corresponding keys are = {info.values()}")
a = info.values()
print(f"here it is = {type(a)}")

# to iterate only on the keys of the dictionary
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

# to get all the items in key value-pair
print(info.items())
# we can iterate over the values in key-pairs
for key, value in info.items():
    print(f"the value at the key {key} is {value}")

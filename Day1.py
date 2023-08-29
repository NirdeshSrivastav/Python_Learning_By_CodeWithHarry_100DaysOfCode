# To print anything in the console screen we use print function
print("hello")

print("Hello My Name is nirdesh shrivastav")

# for a new line w add \n
print("\nI am a student of BCA 3rd year")

print("Hello Bro youo are so 'Handsome' yrr")

print("""\nHello bro
,,I am your jigri Yaar""")

# Escape characters
print("""\n\n^[\w\.-]+@([\w\-]+|\.)+[A-Z0-9]{2,4}(?x)
\#\p{Alpha}\1end-of-line comment""")

# DATATYPES in Python

a = 15
print("\nInteger type = ", a);
print("Type  = ", type(a));

a = 2.5
print("\nFloat type = ", a);
print("Type  = ", type(a));

a = "safal"
print("\nString type = ", a)
print("Type  = ", type(a));

a = True
print("\nBool type = ", a);
print("Type  = ", type(a));

a = [1, 2, 3, 4, 5]
print("\nlist type = ", a);
print("Type  = ", type(a));

a = (10, 20, 30)
print("\nTuple type = ", a)
print("Type  = ", type(a))

a = {'name': 'safal', 'age': 20}
print("\nDict type = ", a)
print("Type  = ", type(a))

a = {1, 2, 3, 4, 5}
print("\nSet type = ", a);
print("Type  = ", type(a));

a = None
print("\nNoneType type = ", a);
print("Type  = ", type(a));

a = 2 + 3j
print('\nComplex type = ', a);
print("Type  = ", type(a));

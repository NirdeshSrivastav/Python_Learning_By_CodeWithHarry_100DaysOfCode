# Convirsion of one datatype to another datatype is called Type Casting

# a = 1
# b = 2
# print(a+b)

a = "1"
b = "2"
print(int(a) + int(b))  # prints 3

# a = "harry"
# b=5
# print(int(a)+int(b))  #Throws an error

# There are two types of typeCasting in python
# Explicit TypeCast
#     User will have to convert the datatypes
a = "1"
b = "2"
print(int(a) + int(b))

# Implicit TypeCast
#     Python automatically converts the types
c = 1.9
d = 8
print(c + d)
# in this program python will convert the small type to the long type for example it will  convert the d to the float datatype to prevent data loss

# -------First lecture--------
# Strings are immutable

# length of a string
name = "Nirdesh"
print(len(name))

# String slicing
# name = "safal,nirdesh"
# include 0 but not 5
print(name[0:5])  # Will take 0 to 5-1
print(name[:4])  # will take 0 to 4-1
print(name[0:])  # python will add length of the name at the second argument like 0 to len(name)
print(name[0:-3])  # Python will act as 0 to len(name)-3
print(name[-1:-3])  # Python will act as len(name)-1 to len(name)-3
print(name[-3:-1])  # Python will act as len(name)-1 to len(name)-1

# Quick quiz
nm = "Harry"
print(nm[-4:-2])

# -------Second lecture--------
a = "Harry"
print(len(a))
print(a.upper())
print(a.lower())

name = "Safal!!!!!!!!!!"
# when you want to trim the ! marks
print(name.rstrip("!"))

# to change a string
print(a.replace("Harry", "John"))

# split() It convert a string to a list for every white space the string will be an element of a list
s1 = "Hello ji kya haal chaal"
print(s1.split(" "))  # OUTPUT =  ['Hello', 'ji', 'kya', 'haal', 'chaal']

# to convert a heading into a professional heading we will use capitalize() function
head = "introduction to jS"
print(head.capitalize())  # It will convert first letter to the uppercase and all letters to the lowercase

# To center a string according to the screen we use center function
str1 = "welcome to the console"
print(str1.center(50))  # adds 50 whitespaces to the left of the string

# to count the occurrence of the string in a string
print(a.count("Harry"))

# Checks if the string is ending with the given string
str1 = "Welcome to the console!!!"
print(str1.endswith("!!!"))  # returns boolean

# checks if the given substring indexes is ending with given string
print(str1.endswith("to", 4, 10))  # returns true

# find() checks the first occurrence of the given string in the given string
str1 = "He's Den.  He is an honest man."
print(str1.find("is"))  # it returns the first index of the string if found else returns -1
print(str1.find("sst"))  # wil return -1

# index() checks the first occurrence of the given string in the given string
str1 = "He's Den.  He is an honest man."
print(str1.index("is"))  # it returns the first index of the string if found else throws an error
# print(str1.index("srivastav")) #Throws a ValueError ERROR

# is alnum() it check that the string is alphanumeric or not
str1 = "welcomeToTheConsole"
print(str1.isalnum())  # returns bool

# isalpha() checks that the string is alpha or not A to Z OR a to z
str1 = "Welcome"
print(str1.isalpha())  # true
str1 = "Welcome00"
print(str1.isalpha())  # false

str1 = "hello world!"
print(str1.islower())  # true
str1 = "Hello World!"
print(str1.islower())  # false

# isprintable() checks that the string contains only printable character or not
str1 = "abdc"
print(str1.isprintable())  # true
str1 = 'adc\n'
print(str1.isprintable())  # false

# isspace() checks that string contains whitespaces
str1 = "              "
print(str1.isspace())  # true
str1 = "shrivastav"
print(str1.isspace())  # false

# istitle() checks that the first letter of each word in string i capital or not?
str1 = "Hi My Name Is Kishan"
print(str1.istitle())  # true

# startswith() checks that the string is starting wil the given string piece or not?
str1 = "Python is a Interpreted Language."
print(str1.startswith("Python"))  # true

# swap() convert lower to upper and vice versa
str1 = "nirdesh"
print(str1.swapcase())

# title() convert the string into title;
str1 = "He's Den.  He is an honest man."
print(str1.title())

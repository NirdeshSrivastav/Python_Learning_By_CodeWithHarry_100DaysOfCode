# to open a file
f = open("myFile.txt", 'r')  # first "file  name" second is the mode =
# r = Read, to read only and throws error if the file does not exist
# w = Write, to write only and creates a new file if the file does not exist
# a = append, to append new elements to the file
# x = create, to create a new file
# t = text,  to open as text 'rt' read in text
# b = text,  to open as binary 'rb' read in text
# 'r' is default

# print(f)

text = f.read()  # to get the content of the file
print(text)
f.close()

# f = open("myFile.txt", 'w')  # it will replace the file text to the given text
# f.write("And handsome also")
# f.close()

# Not good way
# f = open("myFile.txt", 'a')  # it will add the text at last of the file.
# f.write("And handsome also")
#
# # efficient way
# with open("myFile.txt", 'a') as f:  # does not require close
#     f.write("Hay i am in 'with'")

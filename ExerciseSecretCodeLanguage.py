# Write a python program to translate  amessage into secret code language. Use the rules below to translate normal english
# into secret code language -
#
# CODING:
# if the word contains at least three character, remove the first letter and append it at the end
#         now append three random characters at the starting and at the end
# else:
# simply reverse the string
#
# exa = harry = ACHarryhDFG,
#
# DECODING:
# if the word contains less than three characters, reverse it.
# else:
#     remove 3 random characters from the start and end. Now remove the LAST letter AND append it to the beginning
#
# Your program should ask whether you want to code or decode

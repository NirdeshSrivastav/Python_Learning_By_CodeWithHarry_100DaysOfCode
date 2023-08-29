# # loop  works on the iterable objects like -  strings, lists, etc.
# # to iterate over strings
# name = "nirdesh"
#
# for i in name:
#     print(i)
#
# # to execute a single statement again and again
# for i in range(20):
#     print("safal")
#
# # loop with condition
# a = "safal"
# for i in a:
#     print(i)
#     if i == 'f':
#         print("Something Special")
#
# # iterate over a set
# colors = ["Red", "Black", "Blue", "Green"]
# for col in colors:
#     print(col)
#     for i in col:
#         print(i)
#
# # to print numbers
# for i in range(1, 9):
#     print(i)
#
# # to print some numbers
# for i in range(20001):
#     print(i)
#
# for i in range(1, 10, 3):   # third parameter will set the steps where it will print every kth element only.
#     print(i)                # In this it will print 1 4 7.
#
#
i = 1
while i < 3:
    print(i)
    i = i + 1
else:
    print("in else")

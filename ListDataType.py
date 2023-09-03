# marks = [3, 5, 6, "safal", True]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
#
# print(marks[-3])  # will be treated as marks[len(marks)-3 which is 5-3=2 and print 6.
#
# # whether the number is available in the list or not
# if 7 in marks:
#     print("yes")
# else:
#     print("No")
#
# if 6 in marks:
#     print("yes")
# else:
#     print("No")
#
# # Performing the same operation in string also
# if "afal" in "safal":
#     print("yes")
# else:
#     print("no")
#
#
# # To print the whole elements of a list
# print(marks)
# print(marks[:])
# print(marks[1: 4])
# print(marks[1: 4: 2])
#
# # ----- List Comprehension ---
lst = [i*i for i in range(4)]
print(lst)

lst = [i for i in range(10) if i%2 == 0]
print(lst)

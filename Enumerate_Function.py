marks = [12, 56, 32, 98, 12, 45, 1, 4]

index = 0
for mark in marks:
    print(mark)
    if index == 3:
        print("Harry, Awesome")
    index += 1

# Enumerate function is used to get index with the item in the list,set or tuple
for index, mark in enumerate(marks):
    print(mark)
    if index == 3:
        print("Harry, Awesome")

for index, mark in enumerate(marks, start=1):  # now it will act as the third marks not the third index and print the statement when the third mark will be occure
    print(mark)
    if index == 3:
        print("Harry, Awesome")



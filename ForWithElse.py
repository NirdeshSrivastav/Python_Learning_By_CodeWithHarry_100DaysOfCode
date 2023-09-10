# Else will be executed after the loop ends in case of loop break else will not be executed
for i in range(5):
    print(i)
else:
    print("Out of loop")

# Else will be executed after the loop ends in case of loop break else will not be executed
for i in range(5):
    print(i)
    if i == 3:
        break
else:  # Here else will not be executed
    print("Out of loop")

# we can do same thing with while loop
i =1
while i < 5:
    print(i)
    i = i + 1

else:
    print("Loop ended Successfully")

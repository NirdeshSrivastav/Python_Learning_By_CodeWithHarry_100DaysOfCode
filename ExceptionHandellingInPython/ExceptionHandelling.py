a = input("Enter the number = ")
print(f"Multiplication table of the number {a} is = ")
try:
    for i in range(11):
        print(f"{int(a)} * {i} = {int(a)*i} ")
except Exception as e:
    print("Invalide input")
print("SOme imp line of code")
print("End of code")

try:
    num = int(input("Enter an integer = "))
    a=[6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")

except IndexError:
    print("INdex error")

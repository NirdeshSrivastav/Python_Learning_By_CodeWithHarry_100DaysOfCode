import os

# os.chdir("/users")  # to change the directory
# print(f"Path = {os.getcwd()}")  # to get the current working directory

# to print all filed in the folder
folders = os.listdir("data")
i = 1
for folder in folders:
    print(folder)
    print(f"FIle {i}. {os.listdir(f'data/{folder}')}")
    print()
    i += 1

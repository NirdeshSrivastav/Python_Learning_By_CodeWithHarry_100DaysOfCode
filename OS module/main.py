import os

# to create a directory/folder in the set path
# if not os.path.exists("../File Handelling In Python"):  # to check whether the passed dir exists or not
#     os.mkdir("../'File Handelling In Python'")
# else:
#     print("Folder already exists")

# to create 100 folders
# for i in range(0, 100):
#     os.mkdir(f"data/Day{i+1}")

# to rename an existing directory
# os.rename("data", "paisa")

# to rename 100 folders
# for i in range(0, 100):
#     os.rename(f"data/Day{i+1}", f"data/Tutorial {i+1}")

# os.remove("path")  # deletes a directory/file
# os.rmdir("path")  # it deletes a file if that is a directory

# os.remove("../Local/Globle.py")
# os.rmdir("../Local")

print(os.cpu_count())


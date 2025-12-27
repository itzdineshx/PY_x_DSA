# File Detection
import os

file = "Week-01/Day-05/hi.txt"

if os.path.exists(file):
    print(f"There is a file {file} exists")

    if os.path.isfile(file):
        print("This is a file!")
    elif os.path.isdir(file):
        print("This is a Directory!")
else:
    print("There is no file like that")
# Reading File (.txt, .json, .csv)
import json
import csv

file_path = "Week-01/Day-05/hi.txt"
file_path_2 = "Week-01/Day-05/employee.json"
file_path_3 = "Week-01/Day-05/employee.csv"


try:
    with open(file_path_3, "r") as file:
        content = csv.reader(file)
        for chars in content:
            print(chars)

except PermissionError:
    print("First Get Permission to read!")

except FileNotFoundError:
    print("U mf there is no file like that!")
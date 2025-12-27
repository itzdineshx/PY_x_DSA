# Writting in files (.json)
import json

# my employee data
emp_data = {
    "name": "ChatGpt",
    "role" : "Manager",
    "age" : 3
}

file_path = "Week-01/Day-05/employee.json"

try:
    with open(file_path, "w") as file:
        json.dump(emp_data, file, indent=4) # Dump to the json file
        print(f"The file Created at {file_path}")

except FileExistsError:
    print("That file already Exist")
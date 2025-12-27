# Writting in files (.csv)
import csv

# my employee data in 2D array
emp_data = [["Name", "Age", "Role"],
            ["ChatGpt", 4, "Manager"],
            ["Gemini", 3, "Designer"],
            ["Perplexity", 2, "Researcher"]]

file_path = "Week-01/Day-05/employee.csv"

try:
    with open(file_path, "w", newline= "") as file:
        writer = csv.writer(file)
        for row in emp_data:
            writer.writerow(row)
        print(f"The file Created at {file_path}")

except FileExistsError:
    print("That file already Exist")
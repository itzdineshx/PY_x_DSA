# File writting - 

txt_data = "I love python!"
file_path = "Week-01/Day-05/love.txt"

with open(file_path, "w", encoding="utf-8") as file:
    file.write(txt_data) # Writting with w mode
    print("Done!")

with open(file_path, "a", encoding="utf-8") as file:
    file.write("\n" + txt_data) # Appending with a mode

with open(file_path, "r", encoding="utf-8") as f:
    print(f.read()) # Reading with r mode
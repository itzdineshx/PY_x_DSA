# Vote Eligibility Checker(India)

"""This Program checks if a person is eligible to vote based on age"""
age = int(input("Enter your age: "))

while age < 0 or age >= 120:
    print("Age Cannot be negative or greater than 120.")
    age = int(input("Enter your age: "))
    
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")
### This program will perform to find largest of three numbers ###

# Input three numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Compare with the second number
if num2 > num1:
    largest = num2
elif num3 > num2:
    largest = num3
else:
    largest = num1

# Print the largest number
print(f"The largest number is: {largest}")
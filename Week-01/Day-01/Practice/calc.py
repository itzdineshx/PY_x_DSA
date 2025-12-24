#Python mini Calculator

#Initialize variables and Operands
operators = input("Enter operator (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculate based on operator
if operators == '+':
    print(round(num1 + num2, 2))
elif operators == '-':
    print(round(num1 - num2, 2))
elif operators == '*':
    print(round(num1 * num2, 2))
elif operators == '/':
    #Error handling for division by zero
    if num2 != 0:
        print(round(num1 / num2, 2))
    else:
        print("Error! Division by zero.")
else:
    print("Invalid operator!")
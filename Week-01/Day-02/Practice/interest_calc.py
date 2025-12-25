# Python Compound Interest Calculator

from ast import Break
principle_amount = 0
interest_rate = 0
invest_time = 0

while True:
    principle_amount = float(input("Enter the Principle Amount: "))
    if principle_amount <= 0:
        print("Principle Amount must be greater than 0.")
    else:
        break
        
while True:
    interest_rate = float(input("Enter the Interest Rate: "))
    if principle_amount <= 0:
        print("Interest Rate must be greater than 0.")
    else:
        break    
        
while True:
    invest_time = float(input("Enter the invest time in years: "))
    if invest_time <= 0:
        print("invest time must be greater than 0.")
    else:
        break
    
total_ci_amount = principle_amount * ((1+interest_rate/100) ** invest_time)
total_profit = total_ci_amount - principle_amount
print(f"The Amount Balance after {invest_time} years is: {total_ci_amount:.2f}")
print(f"The Total Profit after {invest_time} years is: {total_profit:.2f}")
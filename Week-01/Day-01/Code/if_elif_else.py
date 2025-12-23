amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount = 0.20
elif amount >= 2000:
    discount = 0.10
else:
    discount = 0.05

print(f"Final bill: {amount - (amount*discount)}")

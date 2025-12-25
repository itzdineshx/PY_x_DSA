# Max Number with Conditional Expression
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

max_num = a if (a >= b and a >=c) else (b if b >= c else c)
print(f"The Maximum Number is: {max_num}")

# a compares with b and c => if a max => a
# if a not max => b compares with c => if b max => b 
# else c
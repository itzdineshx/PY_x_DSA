# logical Operators in Python
# and => both the condition to be true if anything false it will result as false o.w True
# or => any one condition to be true it will result as true if both false it will result as false
# not => it will reverse the condition if condition is true it will result as false and vice

a = 14
b = 7
# and Operator
if a > 10 and b < 10: # a and b => True and True => True
    print("Both the Conditions are True")
elif a > 10 and b > 10:
    print("Both the Conditions are False")
else:
    print("One of the Conditions is True")
     
# or Operator
if a > 10 or b < 5: # a or b => True or False => True
    print("At least one of the Conditions is True")
elif a < 10 or b > 10:
    print("Both the Conditions are False")
else:
    print("One of the Conditions is True")
    
# not Operator
if not(a < 10): # not a => not True => False
    print("The Condition is True")
else:
    print("The Condition is False")
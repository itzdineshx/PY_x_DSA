# username Validator
# rules:
# 1. Username must be at least 5 characters long and not exceed 12 characters.
# 2. Username can only contain alphanumeric characters (letters and numbers).  
# 3. Username must start with a letter and not contain any spaces.                                             

user_name = input("Enter a username: ")
is_valid = True

if len(user_name) < 5 or len(user_name) > 12: #1 checks =/<5 or >=/ 12
    is_valid = False
elif not user_name.isalnum(): #2 checks only alphabets and numbers
    is_valid = False
elif not user_name[0].isalpha() or ' ' in user_name: #3 Checks index 0 is letter and no spaces
    is_valid = False

if is_valid:
    print("Valid username")
else:
    print("Invalid username.")
    
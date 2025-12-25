# String operations in Python

s = " hello "
print(s.upper())      # ' HELLO '
print(s.strip())      # 'hello'
print(s.capitalize()) # 'Hello'
print(s.replace("h", "H"))  # ' Hello '
print(s.isalnum())   # False (space is not alphanumeric)
print(s.find("e"))   # 2 (index of 'e')
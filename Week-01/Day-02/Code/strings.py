s = "Hello"
print(type(s))  # <class 'str'>

a = 'single quotes'
b = "double quotes"
c = '''triple quotes'''      # Multi-line string
d = r"raw string \n"         # Raw string (no escaping)
e = f"f-string {2+3}"        # f-string (formatted)

s = "Python"
print(s[0])      # 'P'
print(s[-1])     # 'n'
print(s[1:4])    # 'yth'
print(s[::-1])   # Reverse: 'nohtyP'

s = " hello "
print(s.upper())      # ' HELLO '
print(s.strip())      # 'hello'
print(s.capitalize()) # 'Hello'

name, age = "Dinesh", 20
print(f"Name: {name}, Age: {age}")

s = "hello"
b = s.encode("utf-8")  # bytes
print(b.decode("utf-8"))  # 'hello'

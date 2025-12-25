# strings - These are sequences of characters like a collection

s = "Hello"
print(type(s))  # <class 'str'>
print(list(s))  # ['H', 'e', 'l', 'l', 'o'] 

# Basic String Literals     
a = 'single quotes'
b = "double quotes"
c = '''triple quotes'''      # Multi-line string
d = r"raw string \n"         # Raw string (no escaping)
e = f"f-string {2+3}"        # f-string (formatted)

name, age = "Dinesh", 20
print(f"Name: {name}, Age: {age}")

s = "hello"
b = s.encode("utf-8")  # bytes
print(b.decode("utf-8"))  # 'hello'

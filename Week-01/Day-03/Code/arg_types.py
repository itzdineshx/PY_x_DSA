# Argument Types in Python
# types - positional, default, keyword, arbitrary

# Positional Arguments - the order matters
def greet(name, age):
    print(f"\nHello, {name}! You are {age} years old.")
greet("Dinesh", 20)  # Positional arguments

# Default Arguments - if no value is provided, the default is used
def greet_with_default(name, age=20):
    print(f"\nHello, {name}! You are {age} years old.")
greet_with_default("Dinesh")  # age uses default value
greet_with_default("Dinesh", 21)  # age overridden

# Keyword Arguments - the order does not matter
def greet_with_keywords(name, age):
    print(f"\nHello, {name}! You are {age} years old.")
greet_with_keywords(age=20, name="Dinesh")  # Keyword arguments
greet_with_keywords(age=19, name="Naveen") 

# Arbitrary Arguments - allows passing a variable number of arguments
def greet_multiple(*names):
    for name in names:
        print(f"\nHello, {name}!")
greet_multiple("Dinesh", "Naveen", "Kumar")  # Arbitrary arguments

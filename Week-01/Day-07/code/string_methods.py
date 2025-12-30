### This program will demonstrate working with strings in Python ###
# String → Ordered, immutable, indexed sequence of characters.
"""
String → Ordered, immutable, indexed sequence of characters.

The basic operations in string are:
* Accessing
* Indexing
* Slicing
* Length
* Concatenation
* Repetition
* Membership
* String methods
"""

# Creating a string
my_string = "Python Programming"

print("Original string:")
print(my_string)

# Accessing characters using loop
print("\nAccessing characters in the string:")
for ch in my_string:
    print(ch)

# Accessing characters by index
print("\nAccessing characters by index:")
print("First character:", my_string[0])
print("Last character:", my_string[-1])

# String slicing
print("\nString slicing:")
print("First 6 characters:", my_string[:6])
print("Last 11 characters:", my_string[-11:])
print("Reverse string:", my_string[::-1])

# Length of string
print("\nLength of the string:", len(my_string))

# String concatenation
str1 = "Hello"
str2 = "World"
print("\nConcatenated string:", str1 + " " + str2)

# String repetition
print("\nString repetition:", str1 * 3)

# Membership checking
print("\nCheck if 'Python' exists:", "Python" in my_string)
print("Check if 'Java' exists:", "Java" in my_string)

# String methods
print("\nString methods:")
print("Uppercase:", my_string.upper())
print("Lowercase:", my_string.lower())
print("Title case:", my_string.title())
print("Replace:", my_string.replace("Python", "Java"))
print("Split:", my_string.split())

# Strings are immutable (demonstration)
# my_string[0] = 'J'   # ❌ This will cause TypeError

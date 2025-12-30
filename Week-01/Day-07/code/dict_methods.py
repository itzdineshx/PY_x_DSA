### This program will perform a program to demonstrate working with dictionary in python ###
# Dictionary → Mutable, unordered (insertion-ordered) collection of key–value pairs with unique keys.
"""
The Basic operations in List are:
* Creating
* Accessing
* Modifying
* Adding new key-value pairs
* Deleting a key-value pair
* Checking if a key exists
* Length of a dictionary
* Clearing a dictionary
"""

# Creating a dictionary
my_dict = {'name': 'DINESH', 'age': 19, 'city': 'HEAVEN'}

# Accessing elements of a dictionary
print("Accessing elements of the dictionary:")
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("City:", my_dict['city'])

# Modifying
my_dict['age'] = 20
print("\nModified age:", my_dict['age'])

# Adding
my_dict['gender'] = 'Male'
print("Added gender:", my_dict['gender'])

# Deleting
del my_dict['city']

# Checking if a key exists
if 'age' in my_dict:
    print("\n'age' is present in the dictionary.")
else:
    print("Nothing like that")

# Iterating over keys
print("\nKeys in the dictionary:")
for key in my_dict.keys():
    print(key)
print("That's All!")

# Iterating over values
print("\nValues in the dictionary:")
for value in my_dict.values():
    print(value)
print("That's All!")

# Length
print("\nLength of the dictionary:", len(my_dict))

# Copy
new_dict = my_dict.copy()
print("\nCopied dictionary:", new_dict)

# Clear
new_dict.clear()
print("\nCleared dictionary:", new_dict)
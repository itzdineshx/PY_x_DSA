### This program will perform a program to demonstrate working with Lists in python ###
# List → Ordered, mutable, indexed collection that allows duplicate and heterogeneous elements.
"""
The Basic operations in set are:
* Creating
* Accessing (iteration)
* Adding elements (Append)
* Removing elements (clear)
* Length
* Indexing
* Slicing Methods
* Membership checking
"""

# Create an empty list
my_list = []
print("Empty List:", my_list)

# Append elements to the list
my_list.append(3) # append number 3 to list
my_list.append(6) # append number 6 to list
my_list.append(9) # append number 9 to list
print("List after appending elements:", my_list)

# Remove elements from the list
my_list.remove(3)  # Remove the element 3
print("List after removing element 3:", my_list)

# Create another list
new_list = [1, 4, 3]
print("New List:", new_list)

# Extend the original list by appending all elements from the new list
my_list.extend(new_list)
print("List after extending with new_list:", my_list)

# Remove elements by index
index_to_remove = 1
print(f"List after removing element at index {index_to_remove}:", my_list)

# Clear the list
my_list.clear()
print("List after clearing all elements:", my_list)
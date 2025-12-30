### This program will perform a program to demonstrate working with sets in python ###
# Set → Unordered, mutable collection of unique elements with no indexing.
"""
The Basic operations in set are:
* Creating
* Accessing (iteration)
* Adding elements
* Removing elements
* Length
* Union, Intersection
* Difference, Symmetric Difference
* Membership checking
"""

# Creating a set
my_set = {1, 2, 3, 'a', 'b', 'c'}

print("Original set:")
print(my_set)

# Accessing elements of a set (using loop, since indexing is not allowed)
print("\nAccessing elements of the set:")
for element in my_set:
    print(element)

# Adding elements to a set
print("\nAdding elements to the set:")
my_set.add('d')
print("After adding 'd':", my_set)

# Adding multiple elements
my_set.update([4, 5, 6])
print("After adding multiple elements:", my_set)

# Removing elements from a set
print("\nRemoving elements from the set:")
my_set.remove('a')   # raises error if element not found
print("After removing 'a':", my_set)

# Using discard (safe removal)
my_set.discard('x')  # no error even if element not present
print("After discarding 'x':", my_set)

# Length of a set
print("\nLength of the set:", len(my_set))

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("\nSet1:", set1)
print("Set2:", set2)

# Union
print("\nUnion of set1 and set2:", set1 | set2)

# Intersection
print("Intersection of set1 and set2:", set1 & set2)

# Difference
print("Difference of set1 and set2 (set1 - set2):", set1 - set2)

# Symmetric Difference
print("Symmetric Difference of set1 and set2:", set1 ^ set2)

# Membership checking
print("\nCheck if 2 exists in set1:", 2 in set1)
print("Check if 10 exists in set1:", 10 in set1)

# Removing all elements from a set
my_set.clear()
print("\nAfter clearing the set:", my_set)

# Deleting a set
del my_set   # after deleting, we can't access the set

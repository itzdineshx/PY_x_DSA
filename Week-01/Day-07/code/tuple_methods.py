### This program will perform a program to demonstrate working with tuples in python ###
# Tuple → Ordered, immutable, indexed collection that allows duplicate and heterogeneous elements.
"""
The Basic operations in tuple are:
* Accessing
* Slicing
* Length
* Concatenating
* Unpacking
* Count
* Find
"""
# Creating a tuple
my_tuple = (1, 2, 3, 'a', 'b', 'c')

# Accessing elements of a tuple
print("Accessing elements of the tuple:")
for element in my_tuple:
    print(element)

# Accessing elements by index
print("\nAccessing elements by index:")
print("First element:", my_tuple[0])
print("Second element:", my_tuple[1])
print("Last element:", my_tuple[-1])

# Slicing a tuple
print("\nSlicing a tuple:")
print("First three elements:", my_tuple[:3])
print("Last three elements:", my_tuple[-3:])

# Length of a tuple
print("\nLength of the tuple:", len(my_tuple))

# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated_tuple = tuple1 + tuple2
print("\nConcatenated tuple:", concatenated_tuple)

# Unpacking tuples
x, y, z = (10, 20, 30)
print("\nUnpacked values:")
print("x =", x)
print("y =", y)
print("z =", z)

# Count occurrences of an element
print("\nCount of 'a' in the tuple:", my_tuple.count('a'))

# Find index of an element
print("\nIndex of 'b' in the tuple:", my_tuple.index('b'))

# Checking existence of an element
print("\nCheck if 'd' exists in the tuple:", 'd' in my_tuple)

# Deleting a tuple
del my_tuple #after deleting we can't access the list
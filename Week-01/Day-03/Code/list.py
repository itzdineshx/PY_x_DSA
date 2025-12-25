# Collection - Single var to store multiple values/items'
# List - Ordered collection of items/values, mutable and can be accessed with index
fruits = ["apple", "banana", "cherry", "date"]
print(fruits)

# Index List
print(f"I Like to ate {fruits[1]}")

# Length of list
print(f"Total Fruits Available: {len(fruits)}")

# List looping 
# for fruit in fruits:
#     print("These are the Available Fruits: ")
#     print(fruit)


# Adding items to list
fruits.append("Apple")  # adds to the end and duplicates allowed
print(fruits)

fruits[1] = "blueberry"  # modify item at index 1(Specific Index)
print(fruits)

fruits.insert(2, "kiwi")  # insert at index 2(specific position)
print(fruits)


# Removing items from list
fruits.remove("date")  # removes specific item by value(no return)
print(fruits)

popped_fruit = fruits.pop()  # removes and returns last item
print(f"Popped Fruit: {popped_fruit}")
print(fruits)

# Counting occurrences
apple_count = fruits.count("apple")
print(f"There are no of: {apple_count} apples in the list")
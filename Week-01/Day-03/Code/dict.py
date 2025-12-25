# Dictionary Operations in Python
# Dictionary - Collection of {key:value} pairs, ordered, mutable, indexed by keys, Duplicates Not Allowed(keys must be unique)
 
# Creating a dictionary
student = {
    "name": "Dinesh",
    "age": 21,
    "known_lang": ["Python", "JS"],
    "is_active": True,
    "Aim": "Become a Ai ML Developer"
}

#Displaying the dictionary Values
print(student)
print(f"My name is {student['name']} and I am {student['age']} years old.")
print(f"My known_lang are: {student['known_lang']}")
print(f"My Aim is to: {student['Aim']}")
print(f"I Knows {len(student['known_lang'])} programming languages.")
print(f"I Love {student['known_lang'][0]} ❤.")

# Updating values
student["age"] = 20  # modify existing key value
student["known_lang"].append("C")  # modify list inside dictionary
print(student)

# Retrieving keys and values
keys = student.keys()
values = student.values()
print(f"Student Keys: {keys}")
print(f"Student Values: {values}")

print("--------MY BIO DATA-----------")
for key, value in student.items():
    print(f"{key}: {value}")
print("---------@2025------------")
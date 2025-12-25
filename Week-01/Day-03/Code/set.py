#2. set - Undordered collection of unique items/values, mutable but no index
# set does not allow duplicate values

# Creating a set
programming_languages = {"python","python", "java", "c", "javascript"}
print(programming_languages)
print(f"I like to code in {programming_languages}")

# len
print(f"Total Programming Languages Known: {len(programming_languages)}")

# Adding items to a set
programming_languages.add("C#")  # adds item to set
print(programming_languages)

#print(programming_languages[0]) # Err: No indexing in set
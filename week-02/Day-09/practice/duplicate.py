# Contains Duplicate
nums = [1,1,1,3,3,4,3,2,4,2]  # -> True
seen = set() # Stores Visited Values
for i in nums:
    if i in seen:
        print(True)  # Already in seen? -> Return True
    seen.add(i) # New element? -> Add it
print(False) # Nothing Found? -> False
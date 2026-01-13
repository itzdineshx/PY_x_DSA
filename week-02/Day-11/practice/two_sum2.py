# Goal: Find the indices of Two numbers added is same as target

numbers = [2,7,11,15]
target = 9

# Approach 1 - Brute force:
n = len(numbers)
for i in range(n):
    for j in range(i+1,n):
        if numbers[i]+numbers[j] == target:
            print(i+1, j+1)
            break
"""
Complexity:
Time: O(n^2) - Nested loop
Space: O(1)
"""

# Approach 2 - Two Pointer
l, r = 0, len(numbers) -1
while l < r:
    s = numbers[l] + numbers[r] 
    if s == target: # answer
        print(l + 1, r + 1)
        break
    elif s < target: # move left pointer -> right
        l += 1
    else: # move right pointer -> left
        r -= 1
"""
Complexity:
Time: O(n) - Traversal
Space: O(1)
"""
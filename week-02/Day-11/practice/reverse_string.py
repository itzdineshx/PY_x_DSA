# Goal: To Reverse a String

s = ["h","e","l","l","o"]

# Appoach 1 - Brute force
print(s[::-1])

# Approach 2 - Two Pointer
l ,r = 0 , len(s)-1
while l < r: # Traverse
    s[l], s[r] = s[r], s[l] # swap
    l += 1 # increment left pointer
    r -= 1 # decrement right pointer
print(s)

"""
Complexity:
Time: O(n) - Traversal through arr
Space: O(1) - Operations within arr
""" 
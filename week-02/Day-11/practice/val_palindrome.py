# Goal: To Check if it is a palindrome, or not.

s = "A man, a plan, a canal: Panama"
# Approach 1 - Brute Force
r = "".join(c.lower() for c in s if c.isalnum())
if r == r[::-1]:print(True)
else: print(False)

"""
Complexity:
Time: O(n) - Comprehension
Space: O(n) - cloning
"""

# Approach 2 - Two pointer
left, right = 0, len(s) - 1
while left < right:
    # Skipping alpha num elements
    while left < right and not s[left].isalnum():
        left += 1
    while left < right and not s[right].isalnum():
        right -= 1

    # check it is a palindrome
    if s[left].lower() != s[right].lower():
        print(False)
    left += 1
    right -= 1
print(True)
"""
Complexity:
Time: O(n)
Space: O(1)
"""
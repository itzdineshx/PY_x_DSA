# Pivot element of an array
nums = [1,7,3,6,5,6]
tot = sum(nums)
left = 0

for idx, val in enumerate(nums):
    if left == (tot - left - val):
        print(idx)
    left += val
# return(-1)
"""
Complexity:
Time: O(n)
Space: O(1)
"""
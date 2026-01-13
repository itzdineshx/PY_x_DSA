# Goal: Remove Duplicates from Sorted Array

nums = [1,1,2]

# Approach 1: Brute Force(don't try)
nums[:] = (sorted(set(nums)))
print(len(nums))

"""
Complexity:
Time : O(n) - copy of array
Space: O(1)
"""

j = 0
for i in range(1,len(nums)):
    if nums[i] != nums[j]:
        j += 1
        nums[j] = nums[i]
print(j+1)

"""
Complexity:
Time : O(n) - Traversal
Space: O(1)
"""
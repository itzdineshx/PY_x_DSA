# Majority Element

nums = [3,2,3]
n = len(nums)
# Hash map
cnt = {}
majority = n // 2
for i in nums:
    cnt[i] = cnt.get(i, 0) + 1
    if cnt[i] > majority:
        print(i)
"""
Complexity:
Time: O(n) - Traversal and Hash
Space: O(n) - Storing of element
"""
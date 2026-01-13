# Goal: sorted a squared array
nums = [ 0, -1, -4,  6, 10]

# Approach 1 - Using sorting
sort_arr = [num*num for num in nums]
sort_arr.sort()
print(sort_arr)
"""
Complexity:
Time - O(n log n)
Space - O(n)
"""

# Approach 2 - Using Two pointer
l = 0
r = len(nums)-1
sort_arr = []
while l<=r:
    if abs(nums[l]) < abs(nums[r]):
        sort_arr.append(nums[r]**2)
        r -= 1
    else:
        sort_arr.append(nums[l]**2)
        l += 1
print(sort_arr[::-1])

"""
Complexity:
Time - O(n)
Space - O(n)
"""
# Running sum of an array
nums = [3,5,5,2,7]
n = len(nums)
for i in range(1,n): # 1 -> n
    nums[i] += nums[i-1] #  cumulative = prev + curr
print(nums) 
"""
Complexity: 
Time : O(n)
Space: O(1)
"""
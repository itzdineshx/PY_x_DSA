# Maximum Average Subarray I - Brute force
"""
Algorithm - Brute force`
1. traverse throught the sub arr (i -> k)
2. compute the average of given k size window
3. return avg
"""
nums = [1,12,-5,-6,50,3]
k = 4
n = len(nums)
max_avg = float('-inf')
for i in range(n - k+1):
    avg_sum = sum(nums[i:k+i]) / k
    max_avg = max(max_avg,avg_sum)
    
print(max_avg)

"""
Complexity:
Time: O(nk)
Space: O(1)
"""
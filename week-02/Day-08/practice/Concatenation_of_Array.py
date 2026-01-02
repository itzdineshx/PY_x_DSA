"""
Problem Name   : Concatenation of Array
LeetCode ID    : 1929
Difficulty     : Easy
Example :
    Input: nums = [1,2,1]
    Output: [1,2,1,1,2,1]
    Explanation: The array ans is formed as follows:
    - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
    - ans = [1,2,1,1,2,1]
"""

# Optimal Solution
"""
Algorithm:
---------
1. concatenate the list
2. return the concatenated list
"""

class Solution:
    def getConcatenation(self, nums):
        #conc_arr = nums*2
        conc_arr = nums + nums
        return conc_arr
"""
Time Complexity:
----------------
O(1) – No Traversal

Space Complexity:
-----------------
O(1) – single instance
"""

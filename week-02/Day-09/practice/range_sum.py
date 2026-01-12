# Range Sum Query - Immutable

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        cur = 0
        for i in nums:
            cur += i
            self.prefix.append(cur)

    def sumRange(self, left: int, right: int) -> int:
        r_val = self.prefix[right]
        l_val = self.prefix[left-1] if left > 0 else 0
        range_sum = r_val - l_val
        return range_sum

"""
Complexity:
Time: O(1)
Space: O(n)
"""
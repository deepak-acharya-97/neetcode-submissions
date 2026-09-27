"""
https://leetcode.com/problems/product-of-array-except-self/description/
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        prefix_sum = nums[0]

        for i in range(1, n):
            prefix[i] = prefix_sum
            prefix_sum *= nums[i]

        result = [0]*n

        suffix_sum = nums[-1]
        for i in range(n-2, -1, -1):
            suffix_multiplier = suffix_sum
            result[i] = prefix[i] * suffix_multiplier
            suffix_sum *= nums[i]

        result[-1] = prefix[-1]

        return result

"""
https://neetcode.io/problems/subsets-ii
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        def util(i, subset):
            if i >= n:
                result.append(subset.copy())
                return 
            util(i + 1, subset + [nums[i]])
            while i + 1 < n and nums[i] == nums[i+1]:
                i += 1
            util(i + 1, subset)

        util(0, [])
        return result

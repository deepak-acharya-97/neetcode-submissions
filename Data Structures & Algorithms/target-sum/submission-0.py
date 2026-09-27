"""
https://neetcode.io/problems/target-sum
"""
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}

        def ways(index, current_sum):
            if index == n:
                return 1 if current_sum == target else 0

            if index > n:
                return 0

            if (index, current_sum) in dp:
                return dp[(index, current_sum)]

            total = ways(index + 1, current_sum + nums[index])
            total += ways(index + 1, current_sum - nums[index])

            dp[(index, current_sum)] = total

            return total

        return ways(0, 0)



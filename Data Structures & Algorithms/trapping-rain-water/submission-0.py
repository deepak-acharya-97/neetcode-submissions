"""
https://neetcode.io/problems/trapping-rain-water
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left_max = [0]* n
        right_max = [0]*n

        maximum = height[0]
        for i in range(1, n):
            left_max[i] = maximum
            maximum = max(maximum, height[i])

        maximum = height[-1]
        for i in range(n-1, -1, -1):
            right_max[i] = maximum
            maximum = max(maximum, height[i])
            
        result = 0
        for i in range(1, n-1):
            result += max(min(left_max[i], right_max[i]) - height[i], 0)
            
        return result
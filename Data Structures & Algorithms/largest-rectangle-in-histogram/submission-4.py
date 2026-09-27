"""
https://neetcode.io/problems/largest-rectangle-in-histogram
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        n = len(heights)

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                p_index, p_value = stack.pop()
                max_area = max(max_area, p_value * (index-p_index))
                start = p_index
            stack.append((start, height))

        for index, val in stack:
            max_area = max(max_area, val * (n-index))

        return max_area



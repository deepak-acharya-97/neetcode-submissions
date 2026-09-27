"""
https://neetcode.io/problems/permutations
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        visited = [False] * n
        def util(start, visited, permutations):
            if start >= n:
                result.append(permutations.copy())
                return 
            for ind, val in enumerate(nums):
                if not visited[ind]:
                    visited[ind] = True
                    util(start + 1, visited, permutations + [val])
                    visited[ind] = False
                    
        util(0, visited, [])
        return result
                

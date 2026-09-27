"""
https://neetcode.io/problems/search-2d-matrix
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        
        def stair_case_search():
            i = 0
            j = columns - 1
            while i < rows and j >= 0:
                curr = matrix[i][j]
                if curr == target:
                    return True
                if curr > target:
                    j -= 1
                else:
                    i += 1
            return False
        
        return stair_case_search()

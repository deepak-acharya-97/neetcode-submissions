"""
https://neetcode.io/problems/count-paths
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if not (0 <= i < m and 0 <= j < n):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            dp[(i, j)] = dfs(i+1, j) + dfs(i, j+1)
            return dp[(i, j)]

        return dfs(0, 0)

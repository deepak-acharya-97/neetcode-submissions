class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def is_valid(i, j):
            return 0 <= i < m and 0 <= j < n
        
        def dfs(i, j, dp):
            if i == m-1 and j == n-1:
                return 1
            if not is_valid(i, j):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            dp[(i, j)] = dfs(i+1, j, dp) + dfs(i, j+1, dp)
            return dp[(i, j)]
        dp = {}
        return dfs(0, 0, dp)
        
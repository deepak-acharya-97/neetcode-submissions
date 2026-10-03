class Solution:
    def climbStairs(self, n: int) -> int:

        def dfs(num, dp):
            if num == n:
                return 1
            if num > n:
                return 0
            if num in dp:
                return dp[num]
            dp[num] = dfs(num+1, dp) + dfs(num+2, dp)
            return dp[num]
        dp = {}
        return dfs(0, dp)
        
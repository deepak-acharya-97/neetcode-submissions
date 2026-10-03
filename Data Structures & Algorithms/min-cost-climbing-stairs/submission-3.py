class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        def dfs(i, dp):
            if i >= n:
                return 0
            if i in dp:
                return dp[i]
            dp[i] = cost[i] + min(dfs(i+1, dp), dfs(i+2, dp))
            return dp[i]
        dp = {}
        return min(dfs(0, dp), dfs(1, dp))
        
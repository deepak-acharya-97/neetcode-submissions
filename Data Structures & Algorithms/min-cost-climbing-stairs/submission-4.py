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

        def dfs_bu():
            dp = [0]*(n+1)
            for i in range(2, n+1):
                dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
            return dp[n]
        dp = {}
        # return min(dfs(0, dp), dfs(1, dp))
        return dfs_bu()
        
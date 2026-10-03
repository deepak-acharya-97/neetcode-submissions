class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(i, dp):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i <= 0:
                return 0
            if i in dp:
                return dp[i]
            rob = nums[i] + dfs(i-2, dp)
            do_not_rob = dfs(i-1, dp)
            dp[i] = max(rob, do_not_rob)
            return dp[i]

        def dfs_bu():
            if n == 1:
                return nums[0]
            if n == 2:
                return max(nums[0], nums[1])
            dp = [0] * (n+1)
            dp[1] = nums[0]
            dp[2] = max(nums[0], nums[1])
            for i in range(3, n+1):
                dp[i] = max(nums[i-1] + dp[i-2], dp[i-1])
            return dp[n]
        dp = {}
        # return dfs(n-1, dp)
        return dfs_bu()
        
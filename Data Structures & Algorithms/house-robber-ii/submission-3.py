class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])

        def dfs(i, end_index, dp):
            if i > end_index:
                return 0
            if (end_index - i) == 1:
                return max(nums[i], nums[end_index])
            if i in dp:
                return dp[i]
            rob = nums[i] + dfs(i+2, end_index, dp)
            do_not_rob = dfs(i+1, end_index, dp)
            dp[i] = max(rob, do_not_rob)
            return dp[i]
        dp = {}
        return max(dfs(0, n-2, {}), dfs(1, n-1, {}))
            

        
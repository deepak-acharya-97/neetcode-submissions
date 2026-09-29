class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        

        def dfs(i, current_sum, dp):
            if i < 0:
                return 0
            if i == 0:
                return 1 if current_sum == target else 0
            if (i, current_sum) in dp:
                return dp[(i, current_sum)]
            plus = dfs(i-1, current_sum + nums[i-1], dp)
            minus = dfs(i-1, current_sum - nums[i-1], dp)
            dp[(i, current_sum)] = plus + minus
            return dp[(i, current_sum)]
        dp = {}
        return dfs(n, 0, dp)
        
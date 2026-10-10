class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        lis = 1
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i] and (1 + dp[j] > dp[i]):
                    dp[i] = 1 + dp[j]
                    lis = max(lis, dp[i])
        return lis
        
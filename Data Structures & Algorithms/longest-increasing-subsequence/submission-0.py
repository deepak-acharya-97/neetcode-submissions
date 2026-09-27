from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        def n2():
            lis = 1
            for i in range(1, n):
                for j in range(0, i):
                    if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        lis = max(lis, dp[i])
            print(dp)
            return lis

        return n2()
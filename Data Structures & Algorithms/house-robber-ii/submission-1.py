from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def util_dp(index, arr, dp):
            if index == 2:
                return max(arr[0], arr[1])
            if index == 1:
                return arr[0]
            if index == 0:
                return 0
            if dp[index] != -1:
                return dp[index]
            rob = arr[index - 1] + util_dp(index - 2, arr, dp)
            donotrob = util_dp(index - 1, arr, dp)
            dp[index] = max(rob, donotrob)
            return dp[index]

        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [-1] * (n + 1)
        result1 = util_dp(n - 1, nums[1:], dp)
        dp = [-1] * (n + 1)
        result2 = util_dp(n - 1, nums[:-1], dp)
        return max(result1, result2)

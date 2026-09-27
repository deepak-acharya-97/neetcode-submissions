from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def util(index):
            if index == 2:
                return max(nums[0], nums[1])
            if index == 1:
                return nums[0]
            if index == 0:
                return 0
            rob = nums[index - 1] + util(index - 2)
            donotrob = util(index - 1)
            return max(rob, donotrob)

        def util_dp(index, dp):
            if index == 2:
                return max(nums[0], nums[1])
            if index == 1:
                return nums[0]
            if index == 0:
                return 0
            if dp[index] != -1:
                return dp[index]
            rob = nums[index - 1] + util_dp(index - 2, dp)
            donotrob = util_dp(index - 1, dp)
            dp[index] = max(rob, donotrob)
            return dp[index]
        n = len(nums)
        dp = [-1] * (n+1)
        # return util(len(nums))
        return util_dp(n, dp)

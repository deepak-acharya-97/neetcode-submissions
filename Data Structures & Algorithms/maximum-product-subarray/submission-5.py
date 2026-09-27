"""
https://neetcode.io/problems/maximum-product-subarray
"""
class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        def approach_1():
            n = len(nums)
            dp = [0] * n
            dp[0] = nums[0]

            maximum = float("-inf")
            for i in range(1, n):
                dp[i] = max(dp[i-1]*nums[i], nums[i])
                maximum = max(maximum, dp[i])

            return maximum

        def approach_2_negative_case():
            res = nums[0]
            curr_min, curr_max = 1, 1

            for num in nums:
                temp = curr_max * num
                curr_max = max(curr_max * num, curr_min * num, num)
                curr_min = min(temp, curr_min * num, num)
                res = max(res, curr_max)

            return res

        # return approach_1()
        return approach_2_negative_case()
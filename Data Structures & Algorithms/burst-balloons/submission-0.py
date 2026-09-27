from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums_temp = [1] + nums + [1]
        dp = {}

        def max_coins_util_n_cube_approach(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            dp[(l, r)] = 0
            for i in range(l, r+1):
                coins = nums_temp[l-1] * nums_temp[i] * nums_temp[r+1]
                coins += (max_coins_util_n_cube_approach(l, i-1) + max_coins_util_n_cube_approach(i+1, r))
                dp[(l, r)] = max(coins, dp[(l, r)])
            return dp[(l, r)]

        return max_coins_util_n_cube_approach(1, len(nums_temp)-2)

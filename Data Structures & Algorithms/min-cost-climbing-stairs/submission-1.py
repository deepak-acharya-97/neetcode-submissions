from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        def util(position, dp):
            if position >= n:
                return 0
            if dp[position] != -1:
                return dp[position]

            i1th_step = util(position + 1, dp)
            i2th_step = util(position + 2, dp)
            return cost[position] + min(i1th_step, i2th_step)
        dp = [-1] * n
        return min(util(0, dp), util(1, dp))

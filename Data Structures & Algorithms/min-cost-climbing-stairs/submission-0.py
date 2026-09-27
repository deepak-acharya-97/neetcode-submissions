from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        def util(position):
            if position >= n:
                return 0

            i1th_step = util(position + 1)
            i2th_step = util(position + 2)
            return cost[position] + min(i1th_step, i2th_step)

        return min(util(0), util(1))

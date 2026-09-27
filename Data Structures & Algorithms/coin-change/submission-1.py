"""
https://neetcode.io/problems/coin-change
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = {}

        def util(n, curr_sum):

            if curr_sum == 0:
                return 0

            if n < 1 or curr_sum < 0:
                return float("inf")

            if (n, curr_sum) in dp:
                return dp[(n, curr_sum)]

            if coins[n-1] > curr_sum:
                return util(n-1, curr_sum)

            consider = 1 + util(n, curr_sum - coins[n-1])
            do_not_consider = util(n-1, curr_sum)

            answer = min(consider, do_not_consider)
            dp[(n, curr_sum)] = answer
            return answer

        result = util(len(coins), amount)
        return -1 if result == float("inf") else result

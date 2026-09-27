from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_index = 0
        n = len(prices)
        max_profit = 0
        for i in range(1, n):
            if prices[i] < prices[lowest_index]:
                lowest_index = i
            else:
                profit = prices[i] - prices[lowest_index]
                max_profit = max(max_profit, profit)
        return max_profit

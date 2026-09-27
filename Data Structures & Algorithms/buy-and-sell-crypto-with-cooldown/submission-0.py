from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cooldown_period = 1
        n = len(prices)
        dp = {}
        def dfs(index, buying):
            if index >= n:
                return 0
            
            if (index, buying) in dp:
                return dp[(index, buying)]
            
            #if we are buying we have two options - buy and cooldown
            if buying:
                buy = dfs(index + 1, not buying) - prices[index]
                cooldown = dfs(index + 1, buying)
                dp[(index, buying)] = max(buy, cooldown)
            else:
                sell = dfs(index + cooldown_period + 1, not  buying) + prices[index]
                cooldown = dfs(index+1, buying)
                dp[(index, buying)] = max(sell, cooldown)
                
            return dp[(index, buying)]
        
        return dfs(0, True)
                

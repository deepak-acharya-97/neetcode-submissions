"""
https://neetcode.io/problems/coin-change-ii
"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = {}
        
        def ways(index, target):
            if target == 0:
                return 1
            if index <= 0:
                return 0
            if (index, target) in dp:
                return dp[(index, target)]
            
            if coins[index-1] > target:
                dp[(index, target)] = ways(index-1, target)
                return dp[(index, target)]
            
            consider = ways(index, target-coins[index-1])
            do_not_consider = ways(index-1, target)

            dp[(index, target)] = consider + do_not_consider
            
            return dp[(index, target)]
        
        return ways(n, amount)
            
            
            
            

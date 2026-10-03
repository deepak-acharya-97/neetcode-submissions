from math import isinf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        def dfs(i, amount, dp):
            if amount == 0:
                return 0
            if amount < 0 or i >= n:
                return float("inf")
            
            if (i,amount) in dp:
                return dp[(i, amount)]

            if coins[i] > amount:
                return dfs(i+1, amount, dp)
            dp[(i, amount)] = min(1 + dfs(i, amount-coins[i], dp), dfs(i+1, amount, dp))
            return dp[(i, amount)]
        dp = {}
        ans = dfs(0, amount, dp)
        if isinf(ans):
            return -1
        return ans
        
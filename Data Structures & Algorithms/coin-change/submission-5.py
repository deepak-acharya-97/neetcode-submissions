from math import isinf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        # def dfs(i, amount, dp):
        #     if amount == 0:
        #         return 0
        #     if amount < 0 or i >= n:
        #         return float("inf")
            
        #     if (i,amount) in dp:
        #         return dp[(i, amount)]

        #     if coins[i] > amount:
        #         return dfs(i+1, amount, dp)
        #     dp[(i, amount)] = min(1 + dfs(i, amount-coins[i], dp), dfs(i+1, amount, dp))
        #     return dp[(i, amount)]
        # dp = {}
        # ans = dfs(0, amount, dp)
        # if isinf(ans):
        #     return -1
        # return ans

        def dfs_bu():
            dp = [[float("inf")]*(amount+1) for _ in range(n)]

            for i in range(n):
                for j in range(amount+1):
                    if j == 0:
                        dp[i][j] = 0
                    # elif i == 0 and j <= coins[i]:
                    #     dp[i][j] = 1 if coins[i] == j else float("inf")
                    else:
                        if coins[i] > j:
                            dp[i][j] = dp[i-1][j]
                        else:
                            dp[i][j] = min(1 + dp[i][j-coins[i]], dp[i-1][j])
            return -1 if isinf(dp[-1][-1]) else dp[-1][-1]

        return dfs_bu()
        

                    
        
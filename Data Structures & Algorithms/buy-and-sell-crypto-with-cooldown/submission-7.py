class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        def dfs(i, is_buy, dp):
            print("i>>>>", i, is_buy)
            if i >= n:
                return 0
            if (i, is_buy) in dp:
                return dp[(i, is_buy)]
            if is_buy:
                print("Buying....")
                option = -prices[i] + dfs(i+1, not is_buy, dp)
                print("Anwer = ", i, is_buy, option)
            else:
                print("Selling....")
                option = prices[i] + dfs(i+2, not is_buy, dp)
                print("Anwer = ", i, is_buy, option)
            no_action = dfs(i+1, is_buy, dp)
            dp[(i, is_buy)] = max(option, no_action)
            return dp[(i, is_buy)]
        dp = {}
        return dfs(0, True, dp)
        
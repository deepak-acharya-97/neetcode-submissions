class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        def dfs(i, current_amount, dp):
            if i < 0:
                return 0
            if current_amount < 0 or current_amount > amount:
                return 0
            if i == 0:
                if current_amount == amount:
                    return 1
                return 0
            if (i, current_amount) in dp:
                return dp[(i, current_amount)]
            consider = dfs(i, current_amount + coins[i-1], dp)
            do_not_consider = dfs(i-1, current_amount, dp)
            dp[(i, current_amount)] = consider + do_not_consider
            return dp[(i, current_amount)]
        dp = {}
        return dfs(n, 0, dp)
        
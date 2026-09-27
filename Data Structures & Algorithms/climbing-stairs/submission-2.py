class Solution:
    def climbStairs(self, n: int) -> int:
        def util(stair_position, dp):
            if stair_position < 0:
                return 0
            if stair_position == 0:
                return 1
            if dp[stair_position] != -1:
                return dp[stair_position]
            dp[stair_position] = util(stair_position-1, dp) + util(stair_position-2, dp)
            return dp[stair_position]

        def bottom_up():
            dp = [0] * (n + 1)
            dp[0] = 1
            dp[1] = 1
            for i in range(2, n+1):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[n]

        # dp = [-1] * (n+1)
        # return util(n, dp)
        return bottom_up()

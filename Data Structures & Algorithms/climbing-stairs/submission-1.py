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

        dp = [-1] * (n+1)
        return util(n, dp)

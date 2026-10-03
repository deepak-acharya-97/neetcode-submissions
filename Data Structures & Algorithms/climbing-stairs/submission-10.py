class Solution:
    def climbStairs(self, n: int) -> int:

        def dfs(num, dp):
            if num == n:
                return 1
            if num > n:
                return 0
            if num in dp:
                return dp[num]
            dp[num] = dfs(num+1, dp) + dfs(num+2, dp)
            return dp[num]

        def dfs_bu():
            if n <= 2:
                return n
            dp = [0]*n
            dp[0] = 1
            dp[1] = 2
            for i in range(2, n):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[n-1]

        def dfs_so():
            if n <= 2:
                return n
            one = 1
            two = 2
            result = 0
            for i in range(2, n):
                result = one + two
                one = two
                two = result
            return result

        dp = {}
        # return dfs(0, dp)
        # return dfs_bu()
        return dfs_so()
        
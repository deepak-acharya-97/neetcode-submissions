class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        def lcs(m, n):
            if m == 0 or n == 0:
                return 0
            if (m, n) in dp:
                return dp[(m, n)]

            if text1[m-1] == text2[n-1]:
                dp[(m, n)] = 1 + lcs(m-1, n-1)
                return dp[(m, n)]

            dp[(m, n)] = max(lcs(m-1, n), lcs(m, n-1))
            return dp[(m, n)]

        m, n = len(text1), len(text2)

        def lcs_bottom_up():
            dp = [[0] * (n + 1) for _ in range(m+1)]

            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if text1[i-1] == text2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

            return dp[m][n]

        def lcs_bottom_up_space_optimized():
            prev = [0] * (n + 1)
            curr = [0] * (n + 1)

            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if text1[i-1] == text2[j-1]:
                        curr[j] = 1 + prev[j-1]
                    else:
                        curr[j] = max(prev[j], curr[j-1])
                prev = curr[:]

            return curr[n]

        def lcs_bottom_up_variant_2():
            dp = [[0] * (n + 1) for _ in range(m+1)]

            for i in range(m-1, -1, -1):
                for j in range(n-1, -1, -1):
                    if text1[i] == text2[j]:
                        dp[i][j] = 1 + dp[i+1][j+1]
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j+1])

            return dp[0][0]

        # return lcs(m, n)
        # return lcs_bottom_up()
        # return lcs_bottom_up_variant_2()
        return lcs_bottom_up_space_optimized()

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

        return lcs(m, n)

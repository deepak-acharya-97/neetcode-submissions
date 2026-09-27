class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        def lcs(i, j, dp):
            if i <= 0 or j <= 0:
                return 0
            if text1[i-1] == text2[j-1]:
                return 1 + lcs(i-1, j-1, dp)
            if (i, j) in dp:
                return dp[(i, j)]
            dp[(i, j)] = max(lcs(i-1, j, dp), lcs(i, j-1, dp))
            return dp[(i, j)]
        dp = {}
        return lcs(m, n, dp)
        
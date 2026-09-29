class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        def dfs(i, j, dp):
            if i < 0 or j < 0:
                return 0
            if i == 0:
                return j
            if j == 0:
                return i
            if (i, j) in dp:
                return dp[(i, j)]
            if word1[i-1] == word2[j-1]:
                dp[(i, j)] = dfs(i-1, j-1, dp)
                return dp[(i, j)]
            dp[(i, j)] = 1 + min(min(dfs(i, j-1, dp), dfs(i-1, j, dp)), dfs(i-1, j-1, dp))
            return dp[(i, j)]
        dp = {}
        return dfs(m, n, dp)
        
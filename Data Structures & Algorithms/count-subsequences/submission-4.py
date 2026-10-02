
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        def dfs(i, j, dp):
            if j == n:
                return 1
            if i == m:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            #consider i
            result = 0

            #case 1
            if s[i] == t[j]:
                result += dfs(i+1, j+1, dp)
            result += dfs(i+1, j, dp)
            dp[(i, j)] = result
            return result
        dp = {}
        return dfs(0, 0, dp)
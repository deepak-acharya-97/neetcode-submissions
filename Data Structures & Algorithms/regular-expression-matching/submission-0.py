"""
https://neetcode.io/problems/regular-expression-matching
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        n = len(s)
        m = len(p)

        def dfs(i, j):
            if i >= n and j >= m:
                return True

            if j >= m:
                return False

            if (i, j) in dp:
                return dp[(i, j)]

            current_characters_match = i < n and (s[i] == p[j] or p[j] == '.')

            if (j+1) < m and p[j+1] == '*':
                result = dfs(i, j+2) or (current_characters_match and dfs(i+1, j))
                dp[(i, j)] = result
                return result

            if current_characters_match:
                result = dfs(i+1, j+1)
                dp[(i, j)] = result
                return result

            dp[(i, j)] = False
            return False

        return dfs(0, 0)


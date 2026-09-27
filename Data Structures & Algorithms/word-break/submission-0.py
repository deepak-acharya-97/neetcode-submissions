"""
https://neetcode.io/problems/word-break
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)

        def try_1():
            dp[n] = True
            for ind in range(n-1, -1, -1):
                for word in wordDict:
                    if ind + len(word) - 1 < n and s[ind: ind+len(word)] == word:
                        dp[ind] = dp[ind + len(word)]
                    if dp[ind]:
                        break
            print(dp)
            return dp[0]

        return try_1()


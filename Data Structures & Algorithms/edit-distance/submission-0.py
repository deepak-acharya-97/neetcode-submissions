"""
https://neetcode.io/problems/edit-distance
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        def util(i, j):
            if i == 0:
                return j
            if j == 0:
                return i

            if word1[i-1] == word2[j-1]:
                return util(i-1, j-1)

            return 1 + min(util(i-1, j), util(i, j-1), util(i-1, j-1))

        return util(m, n)



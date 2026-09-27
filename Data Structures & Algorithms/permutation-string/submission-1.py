"""
https://neetcode.io/problems/permutation-string
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m > n:
            return False

        s1_map = [0] * 26
        s2_map = [0] * 26

        for ch in s1:
            s1_map[ord(ch) - ord('a')] += 1

        for i in range(m):
            s2_map[ord(s2[i]) - ord('a')] += 1

        print(s1_map, s2_map)

        if s1_map == s2_map:
            return True

        ind = 1

        while ind + m - 1 < n:
            add = ind + m - 1
            remove = ind - 1
            s2_map[ord(s2[add]) - ord('a')] += 1
            s2_map[ord(s2[remove]) - ord('a')] -= 1
            if s1_map == s2_map:
                return True
            ind += 1

        return False

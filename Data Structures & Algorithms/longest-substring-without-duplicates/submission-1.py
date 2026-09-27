"""
https://neetcode.io/problems/longest-substring-without-duplicates
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        def sliding_window_set():
            substring = set()
            l = 0
            longest = 0

            for r, val in enumerate(s):
                while s[r] in substring:
                    substring.remove(s[l])
                    l += 1
                substring.add(s[r])
                longest = max(longest, r - l + 1)

            return longest

        return sliding_window_set()



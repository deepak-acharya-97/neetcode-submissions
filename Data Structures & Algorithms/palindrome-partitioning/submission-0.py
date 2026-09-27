"""
https://neetcode.io/problems/palindrome-partitioning
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []
        def is_palindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def util(start, parts):
            if start >= n:
                result.append(parts.copy())
                return

            for end in range(start, n):
                if is_palindrome(start, end):
                    util(end + 1, parts + [s[start:end+1]])
        
        util(0, [])
        return result

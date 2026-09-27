"""
https://neetcode.io/problems/combinations-of-a-phone-number
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        n = len(digits)
        if n == 0:
            return []
        result = []
        def util(start, combination):
            if start >= n:
                result.append(combination)
                return
            for possibility in digitToChar[digits[start]]:
                util(start + 1, combination + possibility)

        util(0, "")
        return result
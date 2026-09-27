"""
https://neetcode.io/problems/longest-repeating-substring-with-replacement
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_frequency = 0
        result = 0
        frequency_map = {}
        l = 0

        for r, val in enumerate(s):
            frequency_map[val] = frequency_map.get(val, 0) + 1
            max_frequency = max(max_frequency, frequency_map[val])
            
            while (r - l + 1) - max_frequency > k:
                frequency_map[s[l]] -= 1
                l += 1
            
            result = max(result, r -l + 1)
            
        return result

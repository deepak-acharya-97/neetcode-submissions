class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        max_length = 0
        n = len(s)

        def move_and_update_pointers(l, r):
            nonlocal result, max_length
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > max_length:
                    max_length = (r-l+1)
                    result = s[l:r+1]
                l -= 1
                r += 1

        for i in range(n):
            move_and_update_pointers(i, i)
            move_and_update_pointers(i, i + 1)

        return result



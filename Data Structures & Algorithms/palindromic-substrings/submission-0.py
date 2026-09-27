class Solution:
    def countSubstrings(self, s: str) -> str:
        result = 0
        n = len(s)

        def move_and_update_pointers(l, r):
            nonlocal result
            while l >= 0 and r < n and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1

        for i in range(n):
            move_and_update_pointers(i, i)
            move_and_update_pointers(i, i + 1)

        return result



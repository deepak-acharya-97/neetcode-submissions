class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dp = {}

        def util(index):
            print(f"{index=}")
            if index > n:
                return 0

            if index == n:
                return 1

            if s[index] == "0":
                return 0

            if index in dp:
                return dp[index]

            result = util(index + 1) # consider 1 character

            #consider two characters
            if index + 1 < n and (s[index] == '1' or ( s[index] == '2' and s[index + 1] in "0123456")):
                result += util(index + 2)

            dp[index] = result

            return result

        return util(0)

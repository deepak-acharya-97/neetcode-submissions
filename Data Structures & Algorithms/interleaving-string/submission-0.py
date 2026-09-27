class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        o = len(s3)
        if (m + n) != o:
            return False

        dp = {}

        def util(i, j, k):
            if k == o:
                return i == m and j == n

            if (i, j, k) in dp:
                return dp[(i, j, k)]

            if i < m and s1[i] == s3[k]:
                result = util(i+1, j, k+1)
                if result:
                    dp[(i, j, k)] = True
                    return True

            if j < n and s2[j] == s3[k]:
                result = util(i, j+1, k+1)
                if result:
                    dp[(i, j, k)] = True
                    return True
            dp[(i, j, k)] = False
            return False

        return util(0, 0, 0)

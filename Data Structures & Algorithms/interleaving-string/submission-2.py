class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, o = len(s1), len(s2), len(s3)

        def dfs(i, j, k):
            if i < 0 or j < 0 or k < 0:
                return False
            if i == 0 and j == 0 and k == 0:
                return True
            
            if (i-1) >= 0 and (k-1) >= 0 and s1[i-1] == s3[k-1]:
                return dfs(i-1, j, k-1)
            if (j-1) >= 0 and (k-1) >= 0 and s2[j-1] == s3[k-1]:
                return dfs(i, j-1, k-1)
            return False

        return dfs(m, n, o)
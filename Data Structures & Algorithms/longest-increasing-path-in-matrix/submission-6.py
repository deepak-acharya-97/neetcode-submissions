class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        columns = len(matrix[0])
        adjacents = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def is_valid(i, j):
            return (0 <= i < rows and 0 <= j < columns)

        def dfs(i, j, visited, dp):
            if not (0 <= i < rows and 0 <= j < columns):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            # visited[(i, j)] = True
            max_value = 0
            for (a_i, a_j) in adjacents:
                n_i = i + a_i
                n_j = j + a_j
                if is_valid(n_i, n_j) and matrix[n_i][n_j] > matrix[i][j]:
                    ans = dfs(n_i, n_j, visited, dp)
                    max_value = max(max_value, ans)
            # del visited[(i, j)]
            dp[(i, j)] = max_value + 1
            return dp[(i, j)]
        longest_path = 0
        dp = {}
        for i in range(rows):
            for j in range(columns):
                visited = {}
                longest_path = max(longest_path, dfs(i, j, visited, dp))
        return longest_path


            
        
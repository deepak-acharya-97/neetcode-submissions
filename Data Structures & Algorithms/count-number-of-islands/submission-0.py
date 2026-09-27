from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        adjancents = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        rows = len(grid)
        columns = len(grid[0])

        def is_bound(i, j):
            return 0 <= i < rows and 0 <= j < columns

        def dfs(i, j):
            visited.add((i, j))
            for (ni, nj) in adjancents:
                new_i = i + ni
                new_j = j + nj
                if is_bound(new_i, new_j) and grid[new_i][new_j] == '1' and (new_i, new_j) not in visited:
                    dfs(new_i, new_j)
        islands = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    islands += 1
        return islands

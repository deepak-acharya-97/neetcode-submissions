class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        def is_bound(i, j):
            return 0 <= i < rows and 0 <= j < columns

        neighbours = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(i, j, visited):
            if (i, j) not in visited:
                visited.add((i, j))
                for a_i, a_j in neighbours:
                    n_i, n_j = i + a_i, j+a_j
                    if is_bound(n_i, n_j) and grid[n_i][n_j] == "1" and (n_i, n_j) not in visited:
                        dfs(n_i, n_j, visited)
        visited = set()
        islands = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1" and (i, j) not in visited:
                    islands += 1
                    dfs(i, j, visited)
        return islands



        
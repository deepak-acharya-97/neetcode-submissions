class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        columns = len(grid[0])
        adjacents = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def is_bound(i, j):
            return 0 <= i < rows and 0 <= j < columns

        def bfs(i, j, visited):
            q = deque()
            q.append((i, j))
            visited.add((i, j))
            level = 0

            while q:
                for _ in range(len(q)):
                    (c_i, c_j) = q.popleft()
                    for a_i, a_j in adjacents:
                        n_i, n_j = c_i + a_i, c_j + a_j
                        if is_bound(n_i, n_j) and grid[n_i][n_j] != -1 and grid[n_i][n_j] != 0 and (n_i, n_j) not in visited and (1 + level) < grid[n_i][n_j]:
                            visited.add((n_i, n_j))
                            q.append((n_i, n_j))
                            grid[n_i][n_j] = min(grid[n_i][n_j], 1 + level)
                level += 1
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0:
                    bfs(i, j, set())

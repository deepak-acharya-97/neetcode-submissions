class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        adjacents = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        if rows == 1 and columns == 1:
            return grid[0][0]

        def is_bound(i, j):
            return 0 <= i < rows and 0 <= j < columns

        def bfs(i, j, visited):
            q = deque()
            q.append((i, j))
            visited.add((i, j))
            count = 0
            while q:
                c_i, c_j = q.popleft()
                visited.add((c_i, c_j))
                count += 1                
                for a_i, a_j in adjacents:
                    n_i, n_j = c_i + a_i, c_j + a_j
                    if is_bound(n_i, n_j) and grid[n_i][n_j] == 1 and (n_i, n_j) not in visited:
                        # visited.add((n_i, n_j))
                        q.append((n_i, n_j))
            return count

        def dfs(i, j, visited):
            if (i, j) not in visited:
                visited.add((i, j))
                area = 0
                for a_i, a_j in adjacents:
                    n_i, n_j = i + a_i, j+ a_j
                    if is_bound(n_i, n_j) and grid[n_i][n_j] == 1 and (n_i, n_j) not in visited:
                        area += dfs(n_i, n_j, visited)
                return 1 + area
            else:
                return 0
        
        max_area = 0
        visited = set()

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1 and (i, j) not in visited:
                    result = dfs(i, j, visited)
                    max_area = max(max_area, result)

        return max_area


        
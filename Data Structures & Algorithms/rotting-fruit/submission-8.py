class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        adjacents = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def is_bound(i, j):
            return 0 <= i < rows and 0 <= j < columns
        
        def multi_source_bfs():
            q = deque()
            fresh = 0
            for i in range(rows):
                for j in range(columns):
                    if grid[i][j] == 2:
                        q.append((i, j))
                    elif grid[i][j] == 1:
                        fresh += 1
            if len(q) == 0:
                if fresh != 0:
                    return -1
                return 0
            
            level = 0
            while q:
                for _ in range(len(q)):
                    c_i, c_j = q.popleft()

                    for a_i, a_j in adjacents:
                        n_i, n_j = c_i + a_i, c_j + a_j
                        if is_bound(n_i, n_j) and grid[n_i][n_j] == 1:
                            grid[n_i][n_j] = 2
                            q.append((n_i, n_j))
                            fresh -= 1
                level += 1
            return level - 1 if fresh == 0 else -1

        result = multi_source_bfs()

        # for i in range(rows):
        #     for j in range(columns):
        #         if grid[i][j] == 1:
        #             return -1

        return result



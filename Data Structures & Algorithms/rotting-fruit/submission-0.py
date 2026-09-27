from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_fruits = 0
        rows = len(grid)
        colums = len(grid[0])
        queue = deque()
        neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def is_bound(i, j):
            return 0 <= i < rows and 0 <= j < colums

        for i in range(rows):
            for j in range(colums):
                if grid[i][j] == 1:
                    fresh_fruits += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        time = 0
        while fresh_fruits > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for nr, nc in neighbours:
                    new_r = nr + r
                    new_c = nc + c

                    if is_bound(new_r, new_c) and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        queue.append((new_r, new_c))
                        fresh_fruits -= 1
            time += 1
        return time if fresh_fruits == 0 else -1



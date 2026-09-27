"""
https://neetcode.io/problems/islands-and-treasure
"""
from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        colums = len(grid[0])
        neighbours = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def is_bound(i, j):
            return 0 <= i < rows and 0 <= j < colums

        queue = deque()
        visited = set()

        for i in range(rows):
            for j in range(colums):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
                    

        distance = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                # visited.add((r, c))
                grid[r][c] = distance
                for nr, nc in neighbours:
                    new_r = r + nr
                    new_c = c + nc
                    if is_bound(new_r, new_c) and (new_r, new_c) not in visited and grid[new_r][new_c] != -1:
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
            distance += 1





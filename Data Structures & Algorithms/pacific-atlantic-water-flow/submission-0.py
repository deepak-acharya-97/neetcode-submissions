"""
https://neetcode.io/problems/pacific-atlantic-water-flow
"""
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        rows, columns = len(heights), len(heights[0])

        def dfs(i, j, visited, curr_height):
            if not (0 <= i < rows and 0 <= j < columns) or (i, j) in visited or heights[i][j] < curr_height:
                return
            visited.add((i, j))
            for nr, nc in neighbours:
                n_r = i + nr
                n_c = j + nc
                dfs(n_r, n_c, visited, heights[i][j])

        # start from edge - top and bottom
        for c in range(columns):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])

        # start from edge - left and right
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, columns - 1, atlantic, heights[r][columns - 1])

        intersection = pacific.intersection(atlantic)
        return [[i, j] for (i, j) in intersection]
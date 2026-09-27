from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, columns = len(board), len(board[0])
        neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i, j):
            if not (0 <= i < rows and 0 <= j < columns) or board[i][j] != "O":
                return

            board[i][j] = 'N'
            for nr, nc in neighbours:
                n_r = i + nr
                n_c = j + nc
                dfs(n_r, n_c)

        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][columns-1] == 'O':
                dfs(r, columns-1)

        for c in range(columns):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows-1][c] == 'O':
                dfs(rows - 1, c)

        for i in range(rows):
            for j in range(columns):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'N':
                    board[i][j] = 'O'
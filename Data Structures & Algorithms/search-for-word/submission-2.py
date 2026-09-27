"""
https://neetcode.io/problems/search-for-word
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_length = len(word)
        rows = len(board)
        columns = len(board[0])

        def dfs(row, col, start, visited):
            if start == word_length:
                return True

            if start > word_length:
                return False
            if not (0 <= row < rows and 0 <= col < columns) or (row, col) in visited or board[row][col] != word[start]:
                return False

            visited.add((row, col))
            result = dfs(row + 1, col, start+1, visited) or dfs(row, col + 1, start + 1, visited) or dfs(row-1, col, start + 1, visited) or dfs(row, col - 1, start + 1, visited)
            visited.remove((row, col))
            return result

        for i in range(rows):
            for j in range(columns):
                if dfs(i, j, 0, set()):
                    return True

        return False

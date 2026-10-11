class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        columns = len(board[0])
        adjacents = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def is_bound(i, j):
            return 0 <= i < rows and 0 <= j < columns

        def bfs():
            q = deque()
            for i in range(rows):
                for j in range(columns):
                    if (i == 0 or j == 0 or i == rows - 1 or j == columns - 1) and board[i][j] == 'O':
                        board[i][j] = 'N'
                        q.append((i, j))
                        
            while q:
                c_i, c_j = q.popleft()

                for a_i, a_j in adjacents:
                    n_i, n_j = c_i + a_i, c_j + a_j
                    if is_bound(n_i, n_j) and board[n_i][n_j] == 'O':
                        board[n_i][n_j] = 'N'
                        q.append((n_i, n_j))

            for i in range(rows):
                for j in range(columns):
                    if board[i][j] == 'N':
                        board[i][j] = 'O'
                    elif board[i][j] == 'O':
                        board[i][j] = 'X'
            
        bfs()


        
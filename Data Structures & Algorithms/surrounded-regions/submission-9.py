class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        def flip(row, col):
            stack = [(row, col)]
            while stack:
                r, c = stack.pop()
                board[r][c] = "Y"
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if nr in range(ROWS) and nc in range(COLS) and board[nr][nc] == "O":
                        stack.append((nr, nc))

        # flip non surrounded "O"
        for r in range(ROWS):
            if board[r][0] == "O":
                flip(r, 0)
            if board[r][COLS - 1] == "O":
                flip(r, COLS - 1)
        for c in range(COLS):
            if board[0][c] == "O":
                flip(0, c)
            if board[ROWS - 1][c] == "O":
                flip(ROWS - 1, c)
        
        # flip surrounded
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "Y":
                    board[r][c] = "O"
        # restore non-surrounded "O"
        
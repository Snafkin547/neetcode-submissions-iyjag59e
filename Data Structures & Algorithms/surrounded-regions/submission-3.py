class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        ROWS, COLS = len(board), len(board[0])
        dirs = [(-1, 0), (1,0), (0,-1),(0,1)]
        def search(row, col):
            q = [(row, col)]
            board[row][col] = "T"
            while q:
                r, c = q.pop()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O":
                        q.append((nr, nc))
                        board[nr][nc] = "T"
            return

        for r in range(ROWS):
            if board[r][0] == "O":
               search(r, 0)
            if board[r][COLS -1] == "O":
               search(r, COLS-1)
        for c in range(COLS):
            if board[0][c] == "O":
               search(0, c)
            if board[ROWS-1][c] == "O":
               search(ROWS-1, c)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        
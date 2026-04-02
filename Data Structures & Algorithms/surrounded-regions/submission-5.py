class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        
        def bfs(row, col):
            board[row][col] ='T'
            q = deque([(row, col)])
            while q:
                r, c = q.popleft()
                for dr, dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<ROWS and 0<=nc<COLS and board[nr][nc] == 'O':
                        q.append((nr,nc))
                        board[nr][nc] = 'T'
        for r in range(ROWS):
            if board[r][0] == 'O':
                bfs(r,0)
            if board[r][COLS -1] == 'O':
                bfs(r, COLS -1)
        for c in range(COLS):
            if board[0][c] == 'O':
                bfs(0, c)
            if board[ROWS-1][c] == 'O':
                bfs(ROWS-1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        
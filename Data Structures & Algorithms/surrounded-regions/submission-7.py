class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        
        def bfs(q):
            while q:
                r, c = q.popleft()
                for dr, dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<ROWS and 0<=nc<COLS and board[nr][nc] == 'O':
                        q.append((nr,nc))
                        board[nr][nc] = 'T'
        q = deque()
        for r in range(ROWS):
            if board[r][0] == 'O':
                q.append((r, 0))
                board[r][0] = 'T'
            if board[r][COLS -1] == 'O':
                q.append((r, COLS -1))
                board[r][COLS-1] = 'T'
        for c in range(1, COLS-1):
            if board[0][c] == 'O':
                q.append((0, c))
                board[0][c] = 'T'
            if board[ROWS-1][c] == 'O':
                q.append((ROWS-1, c))
                board[ROWS-1][c] = 'T'
        bfs(q)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        
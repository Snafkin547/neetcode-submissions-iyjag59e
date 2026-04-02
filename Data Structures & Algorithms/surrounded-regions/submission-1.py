class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        ROWS, COLS = len(board), len(board[0])
        dirs = [(-1, 0), (1,0), (0,-1),(0,1)]
        def search(row, col):
            res = False
            q = [(row, col)]
            visiting = set()
            visiting.add((row, col))
            while q:
                r, c = q.pop()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr == -1 or nr == ROWS or nc == -1 or nc == COLS:
                        return
                    elif board[nr][nc] != "X" and (nr, nc) not in visiting:
                        q.append((nr, nc))
                        visiting.add((nr, nc))
            for r, c in visiting:
                board[r][c] = "X"
            return

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    search(r, c)
        
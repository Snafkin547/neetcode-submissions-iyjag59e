class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return True
        if self.size[pu] > self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        return False
    def connected(self, u, v):
        pu, pv = self.find(u), self.find(v)
        return pu == pv

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        dsu = DSU(ROWS* COLS + 1)
            
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != "O":
                    continue
                if r == 0 or r == ROWS - 1 or c == 0 or c == COLS -1:
                    dsu.union(ROWS * COLS, r * COLS + c)
                else:
                    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nr, nc = dr + r, dc + c
                        if board[nr][nc] == "O":
                            dsu.union(nr * COLS + nc, r * COLS + c)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and not dsu.connected(r * COLS + c, ROWS * COLS):
                    board[r][c] = "X"





        
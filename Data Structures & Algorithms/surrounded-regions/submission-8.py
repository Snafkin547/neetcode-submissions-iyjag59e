class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    
    def find(self, node):
        if node!=self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        else:
            if self.size[pu] >= self.size[pv]:
                self.parent[pv] = pu
                self.size[pu] += self.size[pv]
            else:
                self.parent[pu] = pv
                self.size[pv] += self.size[pu]
        return True

    def connected(self, u, v):
        return self.find(u) == self.find(v)
        
class Solution:
    # The idea is to categorize all edge "O"s to a single virtual parent at ROWS * COLS index
    # The second loop flips non-edge "O"s to "X"
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        ROWS, COLS = len(board), len(board[0])
        n = ROWS * COLS
        dsu = DSU(n)
        for r in range(ROWS):
            for c in range(COLS):
                # No ops for "X"
                if board[r][c] == "X":
                    continue
                # Classify edge 'O's to ROWS * COLS
                if r == 0 or r == ROWS-1 or c == 0 or c == COLS -1:
                    dsu.union(r * COLS + c, ROWS * COLS)
                
                # Otherwise, non-edge 'O's to respective parent (could be ROWS * COLS or else where)
                else:
                    for dr, dc in [(-1,0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if board[nr][nc] == "O":
                            dsu.union(r * COLS + c, nr * COLS + nc)
        # Flip non-edge classified 'O's to 'X's
        for r in range(ROWS):
            for c in range(COLS):
                if not dsu.connected(ROWS * COLS, r * COLS + c):
                    board[r][c] = "X"




        
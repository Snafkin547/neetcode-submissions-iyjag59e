class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, i):
        if self.parent[i] != i:
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

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dsu = DSU(ROWS * COLS)
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    for dr, dc in [(1, 0), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                            dsu.union(r * COLS + c, nr * COLS + nc)
                    res = max(res, dsu.size[dsu.find(r * COLS + c)])
                
        return res
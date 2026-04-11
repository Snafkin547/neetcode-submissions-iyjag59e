class DUS:
    def __init__(self, N):
        self.parent = list(range(N))
        self.count = 0

    def find(self, i):
        if i == self.parent[i]:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            self.parent[pv] = pu
            self.count -= 1
        

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        dus = DUS(ROWS * COLS)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dus.count += 1
                    this = r * COLS + c
                    if r != ROWS - 1 and grid[r + 1][c] == "1":
                        below = (r + 1) * COLS + c
                        dus.union(this, below)
                    if c != COLS -1 and grid[r][c + 1] == "1":
                        right = r * COLS + c + 1
                        dus.union(this, right)
        return dus.count
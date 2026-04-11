class DUS:
    def __init__(self, N):
        self.parent = list(range(N))

    def find(self, i):
        if i == self.parent[i]:
            return i
        return self.find(self.parent[i])
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return True
        self.parent[v] = u
        return False

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
                    res += 1
                    # flip 1s
                    stack = [(r, c)]
                    while stack:
                        cr, cc = stack.pop()
                        grid[cr][cc] = "0"
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = cr + dr, cc + dc
                            if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0" or dus.union(cr * COLS + cc, nr * COLS + nc):
                                continue
                            stack.append((nr, nc))
        return res
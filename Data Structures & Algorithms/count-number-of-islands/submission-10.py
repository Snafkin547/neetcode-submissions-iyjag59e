class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
    
    def find(self, node):
        if self.parent[node]!=node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self, u, v):
        up = self.find(u)
        uv = self.find(v)
        if up == uv:
            return False
        else:
            self.parent[up] = uv
        return True
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] 
        res = 0
        dsu = DSU(ROWS * COLS)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if not (0 <= nr < ROWS and 0 <= nc < COLS) or grid[nr][nc] == "0":
                            continue
                        if dsu.union(r * COLS + c, nr * COLS + nc):
                            res -= 1
        return res
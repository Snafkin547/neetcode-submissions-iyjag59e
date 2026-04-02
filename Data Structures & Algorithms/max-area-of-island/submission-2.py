class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                    currRes = 0
                    q = deque()
                    q.append((r, c))
                    while q:
                        cr, cc = q.popleft()
                        if grid[cr][cc]:
                            currRes += 1
                            grid[cr][cc] = 0
                            for dr, dc in dirs:
                                nr, nc = cr + dr, cc + dc
                                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == 0:
                                    continue
                                else:
                                    q.append((nr, nc))
                    res = max(res, currRes)
        return res







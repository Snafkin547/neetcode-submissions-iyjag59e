class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    s = []
                    s.append((row, col))
                    curr = 0
                    while s:
                        cr, cc = s.pop()
                        if cr < 0 or cr >= ROWS or cc < 0 or cc >= COLS or not grid[cr][cc]:
                            continue
                        grid[cr][cc] = 0
                        curr += 1
                        for dr, dc in directions:
                            s.append((cr + dr, cc + dc))
                    res = max(res, curr)
        return res
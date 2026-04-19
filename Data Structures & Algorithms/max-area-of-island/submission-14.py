class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    stack = [(r, c)]
                    curr = 0
                    while stack:
                        row, col = stack.pop()
                        if grid[row][col] == 0:
                            continue
                        curr += 1
                        grid[row][col] = 0
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = dr + row, dc + col
                            if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                                stack.append((nr, nc))
                    res = max(res, curr)
        return res
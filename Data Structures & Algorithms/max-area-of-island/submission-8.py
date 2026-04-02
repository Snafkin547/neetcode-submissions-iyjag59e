class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    stack = [(r, c)]
                    curr = 1
                    grid[r][c] = 0
                    while stack:
                        row, col = stack.pop()
                        for dr, dc in directions:
                            nr, nc = row + dr, col + dc
                            if not (0 <= nr < ROWS and 0 <= nc < COLS) or not grid[nr][nc]:
                                continue
                            else:
                                curr += 1
                                stack.append((nr, nc))
                                grid[nr][nc] = 0
                    res = max(res, curr)
        return res
                
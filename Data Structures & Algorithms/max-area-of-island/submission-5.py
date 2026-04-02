class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or not grid[r][c]:
                return 0
            else:
                curr = 0
                grid[r][c] = 0
                for dr, dc in directions:
                    curr += dfs(r + dr, c + dc)
                return 1 + curr
        for row in range(ROWS):
            for col in range(COLS):
                res = max(res, dfs(row, col))
        return res
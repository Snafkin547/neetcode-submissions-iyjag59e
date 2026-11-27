class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # find 1 and drill down, sum 1s
        # edge case: No grid, single row, 
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0

        def dfs(r, c):
            # flip to 0
            grid[r][c] = 0
            curr = 1
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    curr += dfs(nr, nc)
            return curr            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res 
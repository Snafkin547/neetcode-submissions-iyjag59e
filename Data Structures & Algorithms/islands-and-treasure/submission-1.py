class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2^31 - 1
        directions = [(-1, 0), (1, 0), (0, -1),(0, 1)]
        def dfs(r, c, steps):
            if grid[r][c] < steps: # Including 0 and -1
                return
            grid[r][c] = -1
            for dr, dc in directions:
                nextRow, nextCol = dr + r, dc + c
                if nextRow < 0 or nextRow >= ROWS or nextCol < 0 or nextCol >= COLS or grid[nextRow][nextCol] <= -1:
                    continue
                else:
                    dfs(nextRow, nextCol, 1 + steps)
            grid[r][c] = steps

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    dfs(r, c, 0)
        return
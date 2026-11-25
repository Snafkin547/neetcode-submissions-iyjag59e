class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate over the grid
        # if encounter 1, explore
        # flip visited to 0 so no overlap
        if not grid:
            return 0
        ROW, COL = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def df(r, c):
            grid[r][c] = "0"
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == "1":
                    df(nr, nc)


        res = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    res += 1
                    df(r, c)
        return res            

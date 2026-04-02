class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # If encounter 1, increment res  by 1
        # Start flipping it to 0 all direction
        def flip(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0":
                return
            else:
                grid[r][c] = "0"
                flip(r - 1, c)
                flip(r + 1, c)
                flip(r, c + 1)
                flip(r, c - 1)

        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    res += 1
                    flip(row, col)
        return res
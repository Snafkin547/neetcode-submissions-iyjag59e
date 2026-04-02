class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # If encounter 1, increment res  by 1
        # Start flipping it to 0 all direction
        def flip(r, c):
            if grid[r][c] == "0":
                return
            else:
                grid[r][c] = "0"
                if r > 0:
                    flip(r - 1, c)
                if r < len(grid) - 1:
                    flip(r + 1, c)
                if c < len(grid[0]) - 1:
                    flip(r, c + 1)
                if c > 0:
                    flip(r, c - 1)

        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    res += 1
                    grid[row][col] = "0"
                    if row < len(grid) - 1:
                        flip(row + 1, col)
                    if col < len(grid[0]) - 1:
                        flip(row, col + 1)
        return res
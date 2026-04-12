class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        bananas = 0
        time = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    bananas += 1
        while bananas > 0:
            flag = False
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            row, col = r + dr, c + dc
                            if row in range(ROWS) and col in range(COLS) and grid[row][col] == 1:
                                grid[row][col] = 3
                                bananas -= 1
                                flag = True
            if not flag:
                return -1

            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 3:
                        grid[r][c] = 2
            time += 1
        return time

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2^31 - 1
        directions = [(-1, 0), (1, 0), (0, -1),(0, 1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    stack = [(r, c, 0)]
                    while stack:
                        row, col, steps = stack.pop()
                        if grid[row][col] < steps:
                            continue
                        grid[row][col] = steps
                        for dr, dc in directions:
                            nextRow, nextCol = dr + row, dc + col
                            if nextRow < 0 or nextRow >= ROWS or nextCol < 0 or nextCol >= COLS or grid[nextRow][nextCol] <= 0:
                                continue
                            else:
                                stack.append((nextRow, nextCol, steps + 1))
        return
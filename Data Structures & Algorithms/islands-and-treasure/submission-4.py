class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2**31 - 1
        directions = [(-1, 0), (1, 0), (0, -1),(0, 1)]
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nextRow, nextCol = dr + row, dc + col
                if 0 <= nextRow < ROWS and 0 <= nextCol < COLS and grid[nextRow][nextCol] == INF:
                    grid[nextRow][nextCol] = grid[row][col] + 1
                    q.append((nextRow, nextCol))
        return
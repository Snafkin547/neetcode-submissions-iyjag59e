class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr, nc))
        
        res = 0
        # Check max
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
                res = max(res, grid[r][c])

        return res - 2 if res > 0 else 0
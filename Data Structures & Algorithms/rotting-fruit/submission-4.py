class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    grid[r][c] = 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time = 0
        while fresh and q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    grid[nr][nc] = grid[r][c] - 1
                    q.append((nr, nc))
                    time = max(time, -grid[nr][nc])
                    fresh -= 1
        return time if not fresh else -1

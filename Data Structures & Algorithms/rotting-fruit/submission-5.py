class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # queue up rotten fruit
        # Run multiple BFS
        # Return res if not q else -1
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    grid[r][c] = 0 # Mark rottened 0, so below while can -1
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                # Skip if out of bounds or not fresh 
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc]!=1:
                    continue
                grid[nr][nc] = grid[r][c] - 1
                q.append((nr, nc))

            # Restore original val 0->2
            if grid[r][c] == 0:
                grid[r][c] = 2

        bananas = False
        res = 0
        # Restore original neg -> 1 and find max
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] < 0:
                    res = max(res, -grid[r][c])
                    grid[r][c] = 1
                elif grid[r][c] == 1:
                    bananas = True

        return res if not bananas else -1

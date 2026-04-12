class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # queue up rotten fruit
        # Run multiple BFS
        # Return res if not q else -1
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        bananas = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    grid[r][c] = 0 # Mark rottened 0, so below while can -1
                    q.append((r, c))
                if grid[r][c] == 1:
                    bananas += 1
        res = 0
        while bananas > 0 and q:
            l = len(q)
            for i in range(l):
                r, c = q.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    # Skip if out of bounds or not fresh 
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc]!=1:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    bananas -= 1
            res += 1

        return res if not bananas else -1

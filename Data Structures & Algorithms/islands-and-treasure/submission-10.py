class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # record all chest
        # from recorded chest, traverse and go as much as it can
        # Assuming 2D
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2**31 - 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque([])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        dist = 1
        # increment dist by layer
        # work only INF and within boundary (any normal int is no-go)
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                        grid[nr][nc] = dist
                        q.append((nr, nc))
            dist += 1
                
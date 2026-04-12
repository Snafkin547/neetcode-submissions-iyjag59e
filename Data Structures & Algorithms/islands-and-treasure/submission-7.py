class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # queue up treasure chests
        # Explore/whatever origin reaches first is smallest distance
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2**31 - 1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c, 0))

        # q contains all cells with treasures
        while q:
            r, c, dist = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                # Ignore anything out of bounds and not INF
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != INF:
                    continue
                grid[nr][nc] = dist + 1
                q.append((nr, nc, dist + 1))

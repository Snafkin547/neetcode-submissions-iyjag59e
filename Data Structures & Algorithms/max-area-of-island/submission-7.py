class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    q = deque()
                    grid[r][c] = 0
                    q.append((r, c))
                    curr = 0
                    while q:
                        cr, cc = q.popleft()
                        curr += 1
                        for dr, dc in directions:
                            nextR, nextC = cr + dr, cc + dc
                            if 0 <= nextR < ROWS and 0 <= nextC < COLS and grid[nextR][nextC]:
                                grid[nextR][nextC] = 0
                                q.append((nextR, nextC))
                    res = max(res, curr)
        return res

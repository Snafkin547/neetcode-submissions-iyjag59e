class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # find 1 and drill down, sum 1s
        # edge case: No grid, single row, 
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0           

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    curr = 0 # counter for this island
                    q = deque([(row, col)])
                    grid[row][col] = 0
                    while q:
                        r, c = q.popleft()
                        curr += 1
                        for dr, dc in directions:
                            nr, nc = dr + r, dc + c
                            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                                q.append((nr, nc))
                                grid[nr][nc] = 0

                    # global counter updated
                    res = max(res, curr)
        return res 








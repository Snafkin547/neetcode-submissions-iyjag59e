class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate over the grid
        # if encounter 1, explore
        # flip visited to 0 so no overlap
        if not grid or not grid[0]:
            return 0
        ROW, COL = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        res = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    res += 1
                    grid[r][c] = "0"
                    q = deque([(r, c)])
                    while q:
                        ir, ic = q.popleft()
                        for dr, dc in directions:
                            nr, nc = dr + ir, dc + ic
                            if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                q.append((nr, nc))
                    
        return res            

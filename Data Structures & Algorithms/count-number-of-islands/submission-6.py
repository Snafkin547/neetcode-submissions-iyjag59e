class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            q = deque([(r, c)])
            while q:
                row, col = q.popleft()
                if not (0 <= row < ROWS and 0 <= col < COLS) or grid[row][col] != "1":
                    continue
                grid[row][col] = "0"
                q.append((row + 1, col))
                q.append((row - 1, col))
                q.append((row, col + 1))
                q.append((row, col - 1))
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)
        return res
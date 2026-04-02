class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            st = [(r, c)]
            while st:
                row, col = st.pop()
                for dr, dc in [(1, 0), (-1,0),(0,1),(0,-1)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        st.append((nr, nc))
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)
        return res
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        def dfs(starts):
            visiting = [[False] * COLS for x in range(ROWS)]
            stack = list(starts)
            for r, c in stack:
                visiting[r][c] = True
            while stack:
                r, c = stack.pop()
                for dr, dc in [(1, 0), (-1,0),(0,1),(0,-1)]:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < ROWS and 0 <= nc < COLS) or heights[r][c] > heights[nr][nc] or visiting[nr][nc]:
                        continue
                    else:
                        visiting[nr][nc] = True
                        stack.append((nr, nc))
            return visiting
        res = []
        starts = []
        Astarts = []
        for r in range(ROWS):
            starts.append((r, 0))
            Astarts.append((r, COLS-1))
        for c in range(COLS):
            starts.append((0, c))
            Astarts.append((ROWS-1,c))
        Pac, Atl = dfs(starts), dfs(Astarts)
        for r in range(ROWS):
            for c in range(COLS):
                if Pac[r][c] and Atl[r][c]:
                    res.append([r, c])
        return res

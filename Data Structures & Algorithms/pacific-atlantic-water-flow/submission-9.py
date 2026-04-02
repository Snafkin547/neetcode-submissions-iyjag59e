class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        Atlantic, Pacific = [[False] * COLS for x in range(ROWS)], [[False] * COLS for x in range(ROWS)]

        def dfs(r, c, isPac):
            visiting = Pacific if isPac else Atlantic
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                visiting[r][c] = True
                for dr, dc in [(1, 0), (-1,0),(0,1),(0,-1)]:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < ROWS and 0 <= nc < COLS) or heights[r][c] > heights[nr][nc] or visiting[nr][nc]:
                        continue
                    else:
                        stack.append((nr, nc))
        res = []
        for r in range(ROWS):
            dfs(r, 0, True)
            dfs(r, COLS-1, False)
        for c in range(COLS):
            dfs(0, c, True)
            dfs(ROWS-1,c,False)
        for r in range(ROWS):
            for c in range(COLS):
                if Pacific[r][c] and Atlantic[r][c]:
                    res.append([r, c])
        return res

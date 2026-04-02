class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        Atlantic, Pacific = [[0] * COLS for x in range(ROWS)], [[0] * COLS for x in range(ROWS)]

        def dfs(r, c, isPac):
            visiting = Pacific if isPac else Atlantic
            if visiting[r][c] == 1 or (isPac and (r == 0 or c == 0)) or (not isPac and (r == ROWS - 1 or c == COLS -1)):
                visiting[r][c] = 1
                return True
            
            visiting[r][c] = 2
            reachable = False
            for dr, dc in [(1, 0), (-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < ROWS and 0 <= nc < COLS) or heights[r][c] < heights[nr][nc]:
                    continue
                if visiting[nr][nc] == 2 or visiting[nr][nc] == -1:
                    continue
                elif dfs(nr, nc, isPac):
                    reachable = True
                    break
            visiting[r][c] = 1 if reachable else -1
            return reachable
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, True) and dfs(r,c, False):
                    res.append([r, c])
        return res

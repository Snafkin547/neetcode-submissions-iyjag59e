class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        # 0 unvisited, 2 visiting, 1 possible, -1 impossible
        Pacific, Atlantic = [[0] * COLS for _ in range(ROWS)], [[0] * COLS for _ in range(ROWS)]

        def dfs(r, c, isPacific):
            visiting = Pacific if isPacific else Atlantic
            
            if visiting[r][c] != 0:
                return visiting[r][c] == 1

            if (isPacific and (r == 0 or c == 0)) or (not isPacific and (r == ROWS - 1 or c == COLS -1)):
                visiting[r][c] = 1
                return True
            
            visiting[r][c] = 2
            reachable = False
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[r][c] >= heights[nr][nc]:
                    if dfs(nr, nc, isPacific):
                        reachable = True
                        break
            
            visiting[r][c] = 1 if reachable else -1
            return reachable

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,True) & dfs(r,c,False):
                    res.append([r, c])
        return res


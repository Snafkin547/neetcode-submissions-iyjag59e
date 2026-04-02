class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Explore from Pac and Check intersections/queue
        # Watch equal heights (keep so far max and set while Pac)
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pvisited, avisited = set(), set()

        def dfs(row, col, visited):
            q = deque()
            q.append((row, col))
            visited.add((row, col))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and heights[r][c] <= heights[nr][nc]:
                        visited.add((nr, nc))
                        q.append((nr, nc))
                    

        for i in range(ROWS):
            dfs(i, 0, pvisited)
        for j in range(1, COLS):
            dfs(0, j, pvisited)
        
        for k in range(ROWS):
            dfs(k, COLS - 1, avisited)
        for l in range(0, COLS - 1):
            dfs(ROWS - 1, l, avisited)

        return [list(x) for x in pvisited if x in avisited]

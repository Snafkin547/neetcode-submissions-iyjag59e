class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        visit = [[0] * COLS for _ in range(ROWS)]
        
        q = deque()
        # Start from Pac border
        for r in range(ROWS):
            q.append((r, 0))
        
        for c in range(1, COLS):
            q.append((0, c))
        
        while q:
            r, c = q.popleft()
            visit[r][c] = 1 # Mark as reachable from Pacific border
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                # Only unvisited ones
                if nr in range(ROWS) and nc in range(COLS) and heights[nr][nc] >= heights[r][c] and visit[nr][nc] == 0:
                    q.append((nr, nc))

        # Start from Atl border
        for r in range(ROWS):
            q.append((r, COLS - 1))
        
        for c in range(COLS - 1):
            q.append((ROWS - 1, c))

        res = []
        while q:
            r, c = q.popleft()
            if visit[r][c] == 1: # If a cell is reachable from both
                res.append([r, c])
            visit[r][c] = -1 # Marking this -1 so no overlap
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if nr in range(ROWS) and nc in range(COLS) and heights[nr][nc] >= heights[r][c] and visit[nr][nc] != -1:
                    q.append((nr, nc))
        return res
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Start from 0, a treasure chest, and add steps/min(steps if not new)
        # Keep going unless -1 or curr steps is smaller
        if not grid:
            return 

        ROWS, COLS = len(grid), len(grid[0])
        def dfs(row, col):
            steps = 1
            directions = [(1,0), (-1,0), (0, 1), (0,-1)]
            q = deque([(row, col)])
            while q:
                n = len(q)
                for i in range(n): #The same steps value applies to the same layer
                    row, col = q.popleft()
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if not (0 <= nr < ROWS and 0 <= nc < COLS) or grid[nr][nc] <= steps:
                            continue
                        else:
                            grid[nr][nc] = steps
                            q.append((nr, nc))
                steps += 1        
            return
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    dfs(r, c)
        return
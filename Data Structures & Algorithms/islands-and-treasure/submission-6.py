class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Start from 0, a treasure chest, and add steps/min(steps if not new)
        # Keep going unless -1 or curr steps is smaller
        if not grid:
            return 

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0, 1), (0,-1)]
        
        # Queue up all
        q= deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        # Run BFS once
        while q:
            n = len(q)
            for i in range(n): #The same steps value applies to the same layer
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = grid[row][col] + 1
                        q.append((nr, nc))
        return
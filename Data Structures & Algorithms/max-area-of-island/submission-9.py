class Solution:
    def exploreCurrentIsland(self, r, c, grid):
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        stack = [(r, c)]
        current_area = 1
        grid[r][c] = 0
        while stack:
            row, col = stack.pop()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if not (0 <= nr < ROWS and 0 <= nc < COLS) or not grid[nr][nc]:
                    continue
                else:
                    current_area += 1
                    stack.append((nr, nc))
                    grid[nr][nc] = 0
        return current_area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    max_area = max(max_area, self.exploreCurrentIsland(r, c, grid))
        return max_area
                
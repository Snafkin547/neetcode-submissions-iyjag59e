class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # If encounter 1, increment res  by 1
        # Start flipping it to 0 all direction
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] 
        res = 0
        def flip(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == "0":
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    flip(row, col)
                    res += 1
        return res
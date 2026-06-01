class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        minH = []
        heapq.heappush(minH, (grid[0][0], 0, 0))
        grid[0][0] = float('inf')
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == n - 1 and c == n - 1:
                return t

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if nr in range(n) and nc in range(n) and grid[nr][nc] != float('inf'):
                    heapq.heappush(minH, (max(t, grid[nr][nc]), nr, nc))
                    grid[nr][nc] = float('inf')
        

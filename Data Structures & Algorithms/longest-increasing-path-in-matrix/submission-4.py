class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(matrix), len(matrix[0])
        visited = [[0] * COLS for _ in range(ROWS)]
        def dfs(r, c):
            if visited[r][c]:
                return visited[r][c]
            
            visited[r][c] = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(ROWS) and nc in range(COLS) and matrix[r][c] < matrix[nr][nc]:
                    if visited[nr][nc]:
                        visited[r][c] = max(visited[r][c], 1 + visited[nr][nc])
                    else:
                        visited[r][c] = max(visited[r][c], 1 + dfs(nr, nc))
            return visited[r][c]

        for r in range(ROWS):
            for c in range(COLS):
                if visited[r][c]:
                    res = max(res, visited[r][c])
                else:
                    res = max(res, dfs(r, c))
        return res
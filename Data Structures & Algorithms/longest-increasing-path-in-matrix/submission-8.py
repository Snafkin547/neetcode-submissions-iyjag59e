class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        degree = [[0] * COLS for _ in range(ROWS)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(ROWS):
            for c in range(COLS):
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(ROWS) and nc in range(COLS) and matrix[r][c] > matrix[nr][nc]:
                        degree[r][c] += 1
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if degree[r][c] == 0:
                    q.append((r, c))
        LIS = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(ROWS) and nc in range(COLS) and matrix[r][c] < matrix[nr][nc]:
                        degree[nr][nc] -= 1
                        if degree[nr][nc] == 0:
                            q.append((nr, nc))
            LIS += 1
        return LIS
        
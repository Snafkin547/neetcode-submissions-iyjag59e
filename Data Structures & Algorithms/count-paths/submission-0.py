class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        bd = [[0] * n for i in range(m)]
        bd[0][0] = 1
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                left = 0 if c == 0 else bd[r][c-1]
                above = 0 if r == 0 else bd[r-1][c]
                bd[r][c] = left + above
        return bd[-1][-1]

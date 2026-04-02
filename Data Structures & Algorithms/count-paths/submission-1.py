class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        bd = [1] * n
        for r in range(1, m):
            for c in range(1, n):
                bd[c] += bd[c-1]
        return bd[-1]

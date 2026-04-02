class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        curr = [1] * n
        for row in range(m-1):
            for col in range(n):
                curr[col] += curr[col - 1] if col > 0 else 0
        return curr[-1]

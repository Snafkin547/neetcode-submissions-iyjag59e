class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        mp = defaultdict(int)
        def dfs(i, j):
            if j == n:
                return 1

            if m - i < n - j:
                return 0

            if (i, j) in mp:
                return mp[(i, j)]
            res = 0
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            res += dfs(i + 1, j)
            mp[(i, j)] = res
            return mp[(i, j)]
        return dfs(0, 0)
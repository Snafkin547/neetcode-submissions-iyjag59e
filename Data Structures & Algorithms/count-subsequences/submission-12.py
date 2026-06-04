class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        mp = defaultdict(int)
        def dfs(i, j):
            if j == n:
                return 1
            if i == m:
                return 0
            
            if (i, j) in mp:
                return mp[(i, j)]

            mp[(i, j)] += dfs(i + 1, j)
            if s[i] == t[j]:
                mp[(i, j)] += dfs(i + 1, j + 1)
            return mp[(i, j)]
        return dfs(0, 0)
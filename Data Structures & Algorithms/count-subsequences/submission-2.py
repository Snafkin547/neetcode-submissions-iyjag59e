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
            
            if s[i] == t[j]:
                temp = dfs(i + 1, j + 1)
                if temp != -1:
                    mp[(i, j)] += temp
            temp = dfs(i + 1, j)
            if temp != -1:
                mp[(i, j)] += temp
            if mp[(i, j)] == 0:
                mp[(i, j)] = -1
            return mp[(i, j)]
        res = dfs(0,0)
        return res if res != -1 else 0
        
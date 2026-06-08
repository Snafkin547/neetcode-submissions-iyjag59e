class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = {}
        def dfs(i, j):
            if i == m and j == n:
                return True
            if j == n:
                return False
            if (i, j) in dp:
                return dp[(i, j)]
            match = i < m and (s[i] == p[j] or p[j] == ".")
            dp[(i, j)] = False
            if j + 1 < n and p[j + 1] == "*":
                dp[(i, j)] |= dfs(i, j + 2)
                if match:
                    dp[(i, j)] |= dfs(i + 1, j)
            elif match:
                dp[(i, j)] |= dfs(i + 1, j + 1)
            return dp[(i, j)]
        return dfs(0, 0)
class Solution:

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for l in range(n):
            for i in range(n - l):
                dp[i][i + l] = (s[i] == s[i + l] and
                                    (i + 1 > (i + l - 1) or
                                    dp[i + 1][i + l - 1]))

        res, part = [], []
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if dp[i][j]:
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res
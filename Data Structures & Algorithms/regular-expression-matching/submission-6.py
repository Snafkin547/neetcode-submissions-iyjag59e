class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[-1][-1] = True
        # State: if j can make i
        # next state refer p[j] == s[i] and dp[i + 1][j + 1]
        i, j = m - 1, n - 1
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                match = i < len(s) and (p[j] == s[i] or p[j] == '.')
                if j + 1 < n and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] # Entirely skipping wild card
                    if match:
                        dp[i][j] = dp[i + 1][j] or dp[i][j]
                elif match:
                    dp[i][j] = dp[i + 1][j + 1]
        return dp[0][0]
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[-1][-1] = True
        # State: if j can make i
        for i in range(m, -1, -1): # Handles empty s
            for j in range(n - 1, -1, -1):
                match = i < m and (s[i] == p[j] or p[j] == '.') # Normal match
                if j + 1 < n and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2]
                    if match:
                        dp[i][j] |= dp[i + 1][j]
                elif match:
                    dp[i][j] |= dp[i + 1][j + 1]

        return dp[0][0]
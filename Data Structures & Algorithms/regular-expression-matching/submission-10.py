class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [False] * (n + 1)
        dp[-1] = True
        # State: if j can make i
        for i in range(m, -1, -1): # Handles empty s
            dp1 = dp[-1]
            dp[-1] = (i == m)
            for j in range(n - 1, -1, -1):
                match = i < m and (s[i] == p[j] or p[j] == '.') # Normal match
                res = False
                if j + 1 < n and p[j + 1] == "*":
                    res = dp[j + 2]
                    if match: # for nnn vs n*, current n relies on previous n's result when * involved
                        res |= dp[j]
                elif match: # Simple match
                    res |= dp1
                dp[j], dp1 = res, dp[j]
        return dp[0]

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Empty is met
        for i in range(m + 1):
            dp[0][i] = 1

        # Main loop
        for j in range(1, n + 1):
            for i in range(1, m + 1):
                dp[j][i] = dp[j][i - 1] # If found curr char before, following is always True
                if s[i - 1] == t[j - 1]:
                   dp[j][i] += dp[j - 1][i - 1]
        return dp[-1][-1]


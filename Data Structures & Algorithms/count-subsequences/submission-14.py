class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not s or not t:
            return 0

        m, n = len(s), len(t)
        prev = [1] * (m + 1)

        for j in range(1, n + 1):
            dp = [0] * (m + 1)
            for i in range(1, m + 1):
                dp[i] = dp[i - 1] 
                if s[i - 1] == t[j - 1]:
                   dp[i] += prev[i - 1]
            prev = dp
        return dp[-1]


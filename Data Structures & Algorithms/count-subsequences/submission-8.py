class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        prev = [1] * (m + 1)
        for i in range(n - 1, -1, -1):
            dp = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                res = dp[j + 1]
                if t[i] == s[j]:
                    res += prev[j + 1]
                dp[j] = res
            prev = dp
        return dp[0]
                                
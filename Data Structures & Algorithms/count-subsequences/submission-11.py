class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0

        dp = [1] * (m + 1)
        for i in range(n - 1, -1, -1):
            temp = dp[m]
            dp[m] = 0
            for j in range(m - 1, -1, -1):
                res = dp[j + 1]
                if t[i] == s[j]:
                    res += temp
                temp = dp[j]
                dp[j] = res

        return dp[0]
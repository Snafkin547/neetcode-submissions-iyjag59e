class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not s or not t:
            return 0

        m, n = len(s), len(t)
        dp = [0] * (m + 1)
        for j in range(1, n + 1):
            prev = dp[0]
            for i in range(1, m + 1):
                temp = dp[i - 1] 
                if s[i - 1] == t[j - 1]:
                   temp += prev if j != 1 else 1
                prev, dp[i]= dp[i], temp
        return dp[-1]


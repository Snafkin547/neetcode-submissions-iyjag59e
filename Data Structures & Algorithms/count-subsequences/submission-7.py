class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        prev = [1] * (m + 1)
        
        # if found: diagonal + prev
        for i in range(n - 1, -1, -1):
            curr = False
            dp = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                dp[j] = dp[j + 1]
                if t[i] == s[j]:
                    dp[j] += prev[j + 1]
                    curr = True
            if not curr:
                return 0
            prev = dp
        return prev[0]        
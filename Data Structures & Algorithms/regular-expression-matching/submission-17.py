class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p)
        dp = [False] * (n + 1)
        dp[-1] = True
        for i in range(m, -1, -1):
            nxt_dp = [False] * (n + 1)
            nxt_dp[-1] = (i == m)
            for j in range(n - 1, -1, -1):
                match = i < m and (s[i] == p[j] or p[j] == '.')
                if j + 1 < n and p[j + 1] == '*':
                    nxt_dp[j] = nxt_dp[j + 2]
                    if match:
                        nxt_dp[j] |= dp[j]
                elif match:
                    nxt_dp[j] = dp[j + 1]
            dp = nxt_dp
        
        return dp[0]
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p)
        dp = [False] * (n + 1)
        dp[-1] = True
        # Run from m to cover first * being completely skipped
        for i in range(m, -1, -1):
            nxt_dp = [False] * (n + 1)
            nxt_dp[-1] = (i == m)
            for j in range(n - 1, -1, -1):
                match = i < m and (s[i] == p[j] or p[j] == '.')
                if j + 1 < n and p[j + 1] == '*':
                    # reference one step before to preserve +2 correctness
                    nxt_dp[j] = nxt_dp[j + 2]
                    # if matching, then inherit from i + 1, cuz it could be later than first reference of same repeated char
                    if match:
                        nxt_dp[j] |= dp[j]
                # Simple match should inherit one before i + 1 and j + 1
                elif match:
                    nxt_dp[j] = dp[j + 1]
            dp = nxt_dp
        
        return dp[0]
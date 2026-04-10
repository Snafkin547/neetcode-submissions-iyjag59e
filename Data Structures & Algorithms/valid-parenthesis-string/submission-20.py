# DP(TD, BU)
# Greedy
class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True        
        # state: i and o
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            for o in range(n):
                if s[i - 1] == '(':
                    if o > 0: dp[i][o] |= dp[i - 1][o - 1]
                elif s[i - 1] == ')':
                    if o < n: dp[i][o] |= dp[i - 1][o + 1]
                else:
                    if o > 0: dp[i][o] |= dp[i - 1][o - 1]
                    if o < n: dp[i][o] |= dp[i - 1][o + 1]
                    dp[i][o] |= dp[i - 1][o]
                        
        return dp[-1][0]
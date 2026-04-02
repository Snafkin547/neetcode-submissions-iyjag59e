class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        dp[n][0] = True
        
        for i in range(n - 1, -1, -1):
            for o in range(n):
                res = False
                if s[i] == '*':
                    res |= dp[i + 1][o + 1]
                    if o > 0:
                        res |= dp[i + 1][o - 1]
                    res |= dp[i + 1][o]
                else:
                    if s[i] == '(':
                        res |= dp[i + 1][o + 1]
                    elif o > 0: # when ')' and if there is opening balance
                        res |= dp[i + 1][o - 1]
                dp[i][o] = res
        return dp[0][0]

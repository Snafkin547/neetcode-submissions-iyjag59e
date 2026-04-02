class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n - 1, -1, -1):
            new = [False] * (n + 1)
            for o in range(n):
                res = False
                if s[i] == '*':
                    new[o] = dp[o + 1] or (o > 0 and dp[o - 1]) or dp[o]
                elif s[i] == '(':
                    new[o] = dp[o + 1]
                elif o > 0: # when ')' and if there is opening balance
                    new[o] = dp[o - 1]
            dp = new
        return dp[0]

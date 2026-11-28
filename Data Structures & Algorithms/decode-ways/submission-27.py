class Solution:
    def numDecodings(self, s: str) -> int:
        # if 3 > no carry
        # if not carry and 0, invalid
        # if carry = 2 and > 6 invalid
        n = len(s)
        dp = [0] * (n + 1)
        dp[-1] = 1
        
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                continue
            if i + 1 < n:
                if s[i] == '1' or (s[i] == '2' and s[i + 1] < '7'):
                    dp[i] += dp[i + 2]
            dp[i] += dp[i + 1]
        return dp[0]
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * n
        def dfs(i):
            if i == n:
                return 1
            if dp[i] != -1:
                return dp[i]
                
            if s[i] == '0':
                return 0
            elif i != n - 1 and (s[i] == '1' or (s[i] == '2' and int(s[i + 1]) <= 6)):
                dp[i] = dfs(i + 1) + dfs(i + 2)
            else:
                dp[i] = dfs(i + 1)
            return dp[i]
        return dfs(0)
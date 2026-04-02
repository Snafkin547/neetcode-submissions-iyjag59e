class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * n
        def dfs(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            if dp[i] != -1:
                return dp[i]

            res = 0
            if s[i] == '1' and i + 1 < n:
                res += dfs(i + 2)
            elif s[i] == '2' and i + 1 < n and s[i + 1] in '0123456':
                res += dfs(i + 2)
            res += dfs(i + 1)
            dp[i] = res
            return res
        return dfs(0)
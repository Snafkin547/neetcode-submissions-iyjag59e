class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(idx):
            if idx in dp:
                return dp[idx]
            if s[idx] == '0':
                return 0

            res = dfs(idx + 1)
            if idx + 1 < len(s) and int(s[idx: idx + 2]) <= 26:
                res += dfs(idx + 2)
            dp[idx] = res
            return res

        return dfs(0)
        
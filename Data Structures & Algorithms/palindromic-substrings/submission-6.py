class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        dp = [[False] * n for _ in range(n)]
        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                dp[l][r] = (r - l <= 2 or dp[l + 1][r - 1]) and s[l] == s[r]
                if dp[l][r]:
                    res += 1
        return res
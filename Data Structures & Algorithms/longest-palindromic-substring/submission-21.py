class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        resR, resL = 0, 0
        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                dp[l][r] = (r - l <= 2 or dp[l + 1][r - 1]) and s[l] == s[r]
                if dp[l][r] and r - l > resR - resL:
                    resR, resL = r, l
        return s[resL: resR + 1]
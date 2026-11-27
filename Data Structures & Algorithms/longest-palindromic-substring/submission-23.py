class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # Two types of palindrome: mirro and pivot            
        resL = 0
        resR = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for r in range(n):
            for l in range(r - 1, -1, -1):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    if resR - resL < r - l:
                        resL, resR = l, r
            
        return s[resL : resR + 1]
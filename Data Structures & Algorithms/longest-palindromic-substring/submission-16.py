class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        resIdx = resLen = 0
                        

        for j in range(n):
            for i in range(0, j + 1):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if resLen < j - i + 1:
                        resIdx = i
                        resLen = j - i + 1
        return s[resIdx : resIdx + resLen]
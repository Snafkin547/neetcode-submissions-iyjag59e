class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for size in range(n):
            for i in range(n - size):
                dp[i][i+size] = (
                    s[i] == s[i+size] and
                    (
                        size <= 2 or
                        dp[i + 1][i + size - 1]
                    )
                )
                if dp[i][i+size] and resLen < size:
                    resIdx = i
                    resLen = size
        return s[resIdx: resIdx + resLen + 1]
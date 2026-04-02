class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = s[0]

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i in range(0, n):
            for j in range(i, n):
                if dp[i][j] or isPalindrome(i, j):
                    dp[i][j] = True
                    if len(res) < j - i + 1:
                        res = s[i:j + 1]
        return res
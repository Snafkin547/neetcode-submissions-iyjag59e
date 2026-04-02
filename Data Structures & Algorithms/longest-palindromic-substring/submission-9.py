class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 0

        n = len(s)
        count = 1
        res = s[0]

        for i in range(1, n - 1):
            # odd
            l, r = i - 1, i + 1
            while 0 <= l and r <= n - 1 and s[l] == s[r]:
                if count < r - l + 1:
                    res = s[l:r + 1]
                    count = r - l + 1
                l -= 1
                r += 1
            # even
        for i in range(1, n):
            l, r = i - 1, i
            while 0 <= l and r <= n - 1 and s[l] == s[r]:
                if count < r - l + 1:
                    res = s[l:r + 1]
                    count = r - l + 1
                l -= 1
                r += 1
        return res
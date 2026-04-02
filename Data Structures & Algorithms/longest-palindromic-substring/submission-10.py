class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 0

        n = len(s)
        res = s[0]

        def searchPalindrome(l, r):
            nonlocal res
            while 0 <= l and r <= n - 1 and s[l] == s[r]:
                if len(res) < r - l + 1:
                    res = s[l:r + 1]
                l -= 1
                r += 1

        # odd
        for i in range(1, n - 1):
            l, r = i - 1, i + 1
            searchPalindrome(l, r)
            
        # even
        for i in range(1, n):
            l, r = i - 1, i
            searchPalindrome(l, r)
        return res
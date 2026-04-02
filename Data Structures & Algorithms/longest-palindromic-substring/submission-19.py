class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def findP(l, r):
            while 0 < l and r < n - 1 and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            return l, r + 1

        start, end = 0, 1
        for i in range(n):
            beg, last = findP(i, i)
            if end - start < last - beg:
                start, end = beg, last
            if i < n - 1 and s[i] == s[i + 1]:
                ebeg, elast = findP(i, i + 1)
                if end - start < elast - ebeg:
                    start, end = ebeg, elast
        return s[start: end]
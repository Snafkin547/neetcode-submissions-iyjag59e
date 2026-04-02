class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def findP(l, r):
            while 0 < l and r < n - 1 and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            return s[l:r+1]

        res = ""
        for i in range(n):
            even = findP(i, i)
            if len(res) < len(even):
                res = even
            if i < n - 1 and s[i] == s[i + 1]:
                odd = findP(i, i + 1)
                if len(res) < len(odd):
                    res = odd
        return res
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        resL = resI = 0
        def findP(l, r):
            nonlocal resL, resI
            while 0 <= l and r < n and s[l] == s[r]:
                if r - l + 1 > resL:
                    resL = r - l + 1
                    resI = l
                l -= 1
                r += 1
        for i in range(n):
            findP(i, i)
            findP(i, i + 1)
        return s[resI:resI + resL]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # Two types of palindrome: mirro and pivot            
        resL = 0
        resR = 0
        n = len(s)
        for i in range(n):
            l, r = i, i + 1
            while 0 <= l and r < n and s[l] == s[r]:
                if resR - resL < r - l:
                    resL, resR = l, r
                l -= 1
                r += 1
            
            l, r = i - 1, i + 1
            while 0 <= l and r < n and s[l] == s[r]:
                if resR - resL < r - l:
                    resL, resR = l, r
                l -= 1
                r += 1
        return s[resL : resR + 1]
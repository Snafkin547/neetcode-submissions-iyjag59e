class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPali(string):
            l, r = 0, len(string) - 1
            while l <= r:
                if string[l]!= string[r]:
                    return False
                l, r = l + 1, r -1
            return True

        for size in range(len(s), 0, -1):
            for i in range(len(s) + 1 - size):
                if isPali(s[i: i + size]):
                    return s[i: i + size]
        return ''
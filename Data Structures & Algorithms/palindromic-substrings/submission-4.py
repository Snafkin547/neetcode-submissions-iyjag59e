class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        def isPalindrome(i, isOdd):
            l = i
            r = i if isOdd else i + 1
            count = 0
            while 0 <= l and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        n = len(s)
        res = 0
        for i in range(n):
            res += isPalindrome(i, True)
            res += isPalindrome(i, False)
        return res

    
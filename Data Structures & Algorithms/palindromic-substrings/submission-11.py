class Solution:
    def countSubstrings(self, s: str) -> int:
        res = n = len(s)

        for i in range(n):
            l, r = i, i + 1
            while 0 <= l and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            l, r = i - 1, i + 1
            while 0 <= l and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res
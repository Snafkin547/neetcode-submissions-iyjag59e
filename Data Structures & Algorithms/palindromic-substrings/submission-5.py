class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def helper(l, r):
            count = 0
            while 0 <= l and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        res = 0
        for i in range(n):
            res += helper(i, i) + helper(i, i + 1)
        return res

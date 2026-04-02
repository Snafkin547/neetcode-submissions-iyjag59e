class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0:
            return n
        if n == 0:
            return m

        res = 1
        s = m + n - 2
        i = 1
        while i < n :
            res *= s
            res //= i
            s -= 1
            i += 1
        return res

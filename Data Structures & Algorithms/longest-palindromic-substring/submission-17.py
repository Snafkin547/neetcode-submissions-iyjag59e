class Solution:
    def longestPalindrome(self, s: str) -> str:
        def manchester(st):
            ss = "#" + "#".join(st) + "#"
            n = len(ss)
            l = r = 0
            p = [0] * n
            for i in range(n):
                p[i] = min(r - i, p[l + (r - i)]) if r > i else 0
                while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and ss[i + p[i] + 1] == ss[i - p[i] - 1]:
                    p[i] += 1
                if i + p[i] > r:
                    l, r = i - p[i], i + p[i]
            return p

        p = manchester(s)
        length, idx = max((v, i) for i, v in enumerate(p))
        idx = (idx - length) >> 1
        return s[idx:idx + length]

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = l = freq = 0
        n = len(s)
        chars = defaultdict(int)
        for r in range(n):
            c = s[r]
            chars[c] += 1
            freq = max(freq, chars[c])
            while r - l + 1 - freq > k:
                chars[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
        
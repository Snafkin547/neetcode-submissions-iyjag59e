class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        n = len(s)
        chars = set(s)
        for c in chars:
            l = freq = 0
            for r in range(n):
                if s[r] == c:
                    freq += 1
                while r - l + 1 - freq > k:
                    if s[l] == c:
                        freq -= 1
                    l += 1
                    
                res = max(res, r - l + 1)
        return res
        
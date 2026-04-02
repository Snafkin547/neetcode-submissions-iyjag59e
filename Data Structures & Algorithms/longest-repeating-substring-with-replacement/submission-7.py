class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        cmap, maxf= {}, 0
        l, r = 0, 0
        while r < len(s):
            cmap[s[r]] = 1 + cmap.get(s[r], 0)
            maxf = max(maxf, cmap[s[r]])
            while r - l + 1 - maxf > k: # Contract window to right size
                cmap[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1) # This doesnt get updated when l is shifted
            r += 1

        return res


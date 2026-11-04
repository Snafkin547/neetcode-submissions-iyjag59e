class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Keep track of chars appeared
        # Maintain Max
        # Find dup -> move left till the prev_seen
        n = len(s)
        seen = {}
        res = 0
        l = r = 0
        while r < n:
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            seen[s[r]] = r
            res = max(r - l + 1, res)
            r += 1
        return res
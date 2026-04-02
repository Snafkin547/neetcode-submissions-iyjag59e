class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        mp = {}
        l = r = 0
        n = len(s)
        res = 0
        while r < n:
            if s[r] in mp:
                res = max(res, r - l)
                l = max(mp[s[r]] + 1, l)
            else:
                res = max(res, r - l + 1)
            mp[s[r]] = r
            r += 1
        return res
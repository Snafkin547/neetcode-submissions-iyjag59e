class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        mp = {}

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l) # Moving l to non repeating position
            mp[s[r]] = r # Update where last seen of r
            res = max(res, r - l + 1)
        return res

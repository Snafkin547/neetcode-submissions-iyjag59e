class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # By maintaining the latest index of each appeared char in a map, skip unnecessary move and jump to the next index
        n = len(s)
        mp = {}
        l = 0
        res = 0
        for r in range(n):
            # Update left pointer to the latest index of the curr char or maintain it
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            
            # Record latest index of the curr char
            mp[s[r]] = r
            
            # Maintain max dup free length
            res = max(res, r - l + 1)
        return res

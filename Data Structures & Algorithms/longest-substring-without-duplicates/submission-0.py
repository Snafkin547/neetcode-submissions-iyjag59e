class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        # Sliding window till it's 0 length/break early if found
        # parent loop l goes down to 0
        ## starting point from 0 till i + l < len(s)
        ### Check by comparing length of set and this length, if true, found
        res = 0
        while l > 0:
            i = 0
            while i + l <= len(s):
                charSet = set(s[i:i+l])
                if len(charSet) == l:
                    res = max(l, res)
                i += 1
            l -= 1
        return res
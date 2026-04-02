class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Continue till all included chars appear in the current substring: Check How many in Dict & Queue
        # Count # of appearance of each char: Dict
        # Use Set to count how many more chars to visit till ending the current substring
        mp = {}
        for i, c in enumerate(s):
            mp[c] = i
        res = []
        size = end  = 0
        
        for i, c in enumerate(s):
            size += 1
            end = max(end, mp[c])
            if end == i:
                res.append(size)
                size = 0
        return res
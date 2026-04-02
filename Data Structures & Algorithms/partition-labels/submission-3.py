class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Continue till all included chars appear in the current substring: Check How many in Dict & Queue
        # Count # of appearance of each char: Dict
        # Use Set to count how many more chars to visit till ending the current substring
        mp = Counter(s)
        l = 0
        res = []
        curr = set()
        for r in range(len(s)):
            if s[r] not in curr:
                curr.add(s[r])
            mp[s[r]] -= 1
            if mp[s[r]] == 0:
                curr.discard(s[r])
            if not curr:
                res.append(r - l + 1)
                l = r + 1
        return res
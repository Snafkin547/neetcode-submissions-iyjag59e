class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Find end of chars = Know # of occurance
        # Keep track of which chars included now
        # If # of Occr = 0 and no balance for 
        charMap = Counter(s)
        charSet = set()
        cnt = 0 
        res = []
        for c in s:
            charMap[c] -= 1
            cnt += 1
            if not charMap[c]:
                charSet.discard(c)
                if not charSet:
                    res.append(cnt)
                    cnt = 0
            else:
                charSet.add(c)

        if cnt > 0:
            res.append(cnt)

        return res
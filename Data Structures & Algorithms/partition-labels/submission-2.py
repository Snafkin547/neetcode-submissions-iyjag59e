class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Find end of chars = Know # of occurance
        # Keep track of which chars included now
        # If # of Occr = 0 and no balance for 
        charMap = {}
        for i, c in enumerate(s):
            charMap[c] = i
        cnt = end = 0 
        res = []

        for i, c in enumerate(s):
            cnt += 1
            end = max(end, charMap[c])

            if i == end:
                res.append(cnt)
                cnt = 0
        return res
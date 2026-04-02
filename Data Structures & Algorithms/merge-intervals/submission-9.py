class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Find the max starting val and make a list of that length + 1
        # why + 1: because start index is 0 start:if maxVal = 5 and make a list length 5
        maxVal = max(interval[0] for interval in intervals)
        mp = [0] * (maxVal + 1)
        # register max end for each start/index
        for start, end in intervals:
            mp[start] = max(mp[start], end + 1) # A: +1 avoids mixing up interval that touches and 0 interval like [0, 0]

        # iterate over the list
        start = ending = -1
        res = []
        for i in range(len(mp)):
            if mp[i] != 0: # A': this would miss [0, 0] if not implemented like A
                if start == -1: # if start not initiated, register
                    start = i
                ending = max(mp[i] -1, ending) # A': -1 corresponds to A
            # if idx < ending, meaning there is an overlap or no intvals exist
            if i == ending:
                res.append([start, ending])
                ending = -1
                start = -1

        if ending != -1:
            res.append([start, ending])
        return res
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        elif len(intervals) == 1:
            return 1
        # Keep track of how many ongoing
        maxE = 0
        for u in intervals:
            maxE = max(maxE, u.end)
        
        arr = [0] * (maxE + 1)

        for u in intervals:
            arr[u.start] += 1
            arr[u.end] -= 1
        curr = res = 0
        for v in arr:
            curr += v
            res = max(res, curr)
        return res

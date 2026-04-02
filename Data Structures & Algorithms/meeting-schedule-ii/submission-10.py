"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for v in intervals:
            s, e = v.start, v.end
            time.append((s, 1))
            time.append((e, -1))
        time.sort(key=lambda x: (x[0], x[1]))
        
        res = curr = 0
        for t in time:
            curr += t[1]
            res = max(res, curr)
        return res
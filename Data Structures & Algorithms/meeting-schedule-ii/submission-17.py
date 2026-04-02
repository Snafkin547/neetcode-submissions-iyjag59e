"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Know how many has started before the current end = rooms
        time = []
        for i in intervals:
            time.append((i.start, 1))
            time.append((i.end, -1))
        
        time.sort(key = lambda x: (x[0], x[1]))
        curr = res = 0
        for t, k in time:
            curr += k
            res = max(res, curr)
        return res
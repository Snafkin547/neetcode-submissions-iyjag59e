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
        start, end = [], []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        
        start.sort()
        end.sort()
        curr = res = 0
        s = e = 0
        n = len(intervals)
        while s < n and e < n:
            if start[s] < end[e]:
                curr += 1
                s += 1
            else:
                curr -= 1
                e += 1
            res = max(res, curr)
        return res

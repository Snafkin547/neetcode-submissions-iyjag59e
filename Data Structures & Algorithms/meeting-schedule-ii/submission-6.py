"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s, e = 0, 0
        res, cnt = 0, 0
        while s < len(start):
            if start[s] < end[e]:
                cnt += 1
                s += 1
            else:
                e += 1
                cnt -= 1
            res = max(res, cnt)
        return res
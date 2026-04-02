"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        minH = []
        res = 0
        for i in intervals:
            if minH and minH[0] <= i.start:
                heapq.heappop(minH)
            heapq.heappush(minH, i.end)
            res = max(res, len(minH))

        return res
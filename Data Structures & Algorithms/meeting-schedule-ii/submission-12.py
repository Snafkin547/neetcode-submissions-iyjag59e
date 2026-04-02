"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minH = []
        intervals.sort(key = lambda x: x.start)
        for interval in intervals:
            if minH and minH[0] <= interval.start:
                heapq.heappop(minH)
            heapq.heappush(minH, interval.end)
        return len(minH)
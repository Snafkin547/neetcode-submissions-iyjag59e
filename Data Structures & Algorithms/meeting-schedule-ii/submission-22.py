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
        minH = []
        intervals.sort(key = lambda x:x.start)
        for i in intervals:
            if minH and minH[0] <= i.start:
                heapq.heappop(minH)
            heapq.heappush(minH, i.end)
        return len(minH)
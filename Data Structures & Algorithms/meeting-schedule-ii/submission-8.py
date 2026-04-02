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
        mh = [i.end for i in intervals]
        heapq.heapify(mh)
        for i in intervals:
            if i.start >= mh[0]:
                heapq.heappop(mh)
        return len(mh)


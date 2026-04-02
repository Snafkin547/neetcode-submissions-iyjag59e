"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # incremen and decrement stat and end respectively
        # loop over doct in sorted order
        # keep counting sum so far and update max
        # this should work because if no overlap, then the sum is alwas 0
        timeMap = defaultdict(int)
        for interval in intervals:
            timeMap[interval.start] += 1
            timeMap[interval.end] -= 1
        
        res = 0
        cnt = 0
        for t in sorted(timeMap):
            cnt += timeMap[t]
            res = max(res, cnt)
        return res

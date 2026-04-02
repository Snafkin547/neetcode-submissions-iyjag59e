"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        arr = defaultdict(int)
        for u in intervals:
            arr[u.start] += 1
            arr[u.end] -= 1
        
        curr = res = 0
        for k in sorted(arr.keys()):
            curr += arr[k]
            res = max(res, curr)
        return res

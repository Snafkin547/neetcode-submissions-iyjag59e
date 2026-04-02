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
        mp = defaultdict(int)
        for v in intervals:
            s, e = v.start, v.end
            mp[s] += 1
            mp[e] -= 1
        
        res = curr = 0
        for i in sorted(mp):
            curr += mp[i]
            res = max(res, curr)
        return res
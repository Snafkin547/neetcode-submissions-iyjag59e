"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i:i.start)
        curr = 0
        for i in range(len(intervals)):
            if curr > intervals[i].start:
                return False
            else:
                curr = intervals[i].end
        return True
    

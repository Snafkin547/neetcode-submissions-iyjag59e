"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        new_intvals = []
        for intv in intervals:
            new_intvals.append([intv.start, intv.end])
        new_intvals.sort()
        curr = 0
        for i in range(len(new_intvals)):
            if curr > new_intvals[i][0]:
                return False
            else:
                curr = new_intvals[i][1]
        return True
    

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# Store removals and continue till empty
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        days = 0
        intervals.sort(key = lambda x : x.start) # Sorted by end time
        removed = [interval for interval in intervals] # Copy
        
        while removed:
            days += 1
            currEnd = removed[0].end
            temp = []
            for i in range(1, len(removed)):
                if removed[i].start < currEnd:
                    temp.append(removed[i])
                else:
                    currEnd = removed[i].end
            removed = [interval for interval in temp] # Copy the balance
        return days
            


        
        
# Greedy sort by start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            if prevEnd <= start:
                # Success: Move to next index
                prevEnd = end
            else:
                # If fails, need to count toward removal
                res += 1
                prevEnd = min(end, prevEnd) # Continue working on the smallest end
        return res
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        currEnd = intervals[0][1]
        res = 0
        for s, e in intervals[1:]:
            if currEnd <= s:
                currEnd = e
            else:
                res += 1
                currEnd = min(currEnd, e)
        return res
        
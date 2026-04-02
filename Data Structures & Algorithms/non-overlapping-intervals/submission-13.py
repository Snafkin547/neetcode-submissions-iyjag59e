class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        currEnd = intervals[0][1]
        res = 0
        for s, e in intervals[1:]:
            if s < currEnd:
                res += 1
            else:
                currEnd = e
        return res
        
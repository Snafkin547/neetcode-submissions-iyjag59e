class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key=lambda x: (x[1], x[0]))
        prev = -50001
        # As long as curr start < prev end, remove
        for curr in intervals:
            if prev > curr[0]:
                res += 1
            else:
                prev = curr[1]
        
        return res

# Consider merge firts and eliminate overlapping
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Insert
        l, r = 0, len(intervals)
        newStart = newInterval[0]
        while l < r:
            mid = l + ((r - l) >> 1)
            if intervals[mid][0] < newStart:
                l = mid + 1
            else:
                r = mid
        
        intervals.insert(l, newInterval)

        # Merge
        res = []
        res.append(intervals[0])
        i = 1
        while i < len(intervals):
            start_i, end_i = intervals[i][0], intervals[i][1]
            if start_i <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end_i)
            else:
                res.append(intervals[i])
            i += 1
        return res

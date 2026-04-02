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
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

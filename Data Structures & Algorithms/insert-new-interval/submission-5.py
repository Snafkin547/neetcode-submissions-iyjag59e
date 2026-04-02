class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        l, r = 0, n
        while l < r:
            mid = l + (r - l)//2
            if intervals[mid][0] < newInterval[0]:
                l = mid + 1
            else:
                r = mid
        intervals.insert(l, newInterval)
        res = []
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res
        
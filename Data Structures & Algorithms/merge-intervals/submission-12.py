class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return [[]]
        intervals.sort(key = lambda x: x[0])
        res = []
        curr = intervals[0]
        for interval in intervals[1:]:
            if curr[1] >= interval[0]:
                curr[0] = min(interval[0], curr[0])
                curr[1] = max(interval[1], curr[1])
            else:
                res.append(curr)
                curr = interval
        res.append(curr)
        return res

        
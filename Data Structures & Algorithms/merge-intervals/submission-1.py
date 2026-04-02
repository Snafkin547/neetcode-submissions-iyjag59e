class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # Sort
        intervals.sort(key = lambda x: x[0])
        # Merge
        res = []
        curr = intervals[0]
        for i in range(1, len(intervals)):
            # If not overlapping
            if curr[1] < intervals[i][0]:
                res.append(curr)
                curr = intervals[i]
            # If overlapping
            else:
                curr = [
                    min(curr[0], intervals[i][0]),
                    max(curr[1], intervals[i][1])
                    ]
        res.append(curr)
        return res
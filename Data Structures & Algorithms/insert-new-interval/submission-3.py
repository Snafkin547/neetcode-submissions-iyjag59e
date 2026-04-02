# One pass
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # Suffix: beyond newInterval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            # Prefix
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            
            # Merge Overlapping
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                    ]

        res.append(newInterval)
        return res
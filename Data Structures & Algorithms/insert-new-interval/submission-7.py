class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = [[-1, -1]]

        for i, curr in enumerate(intervals):
            # Found spot for New
            if newInterval[0] <= curr[0]:
                # Overlap with curr
                if curr[0] <= newInterval[1]:
                    curr = [newInterval[0], max(curr[1], newInterval[1])]
                    if res[-1][1] < curr[0]:
                        res.append(curr)
                    else:
                        res[-1][1] = max(res[-1][1], curr[1])
                # No overlap with curr
                else:
                    if res[-1][1] < newInterval[0]:
                        res.append(newInterval)
                        return res[1:] + intervals[i:]
                    else:
                        res[-1][1] = max(res[-1][1], newInterval[1])
                        res.append(curr)
                newInterval = [float('inf'), float('inf')]
            # Work on curr
            else:
                if res[-1][1] < curr[0]:
                    res.append(curr)
                else:
                    res[-1][1] = max(res[-1][1], curr[1])
        
        if newInterval[1]!=float('inf'):
            if res[-1][1] < newInterval[0]:
                res.append(newInterval)
            else:
                res[-1][1] = max(res[-1][1], newInterval[1])
        return res[1:]
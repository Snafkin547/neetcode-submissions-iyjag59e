class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if new[0] is less than curr[1] merge => curr[1] = max(new[1], curr[1])
        # if new[0] < curr[0]:swap
        # if new[0] < curr[1]: merge -> new
        # if curr[1] < new[0]: append curr
        
        res = []
        for i in range(len(intervals)):
            curr = intervals[i]
            if newInterval[1] < curr[0]:
                res.append(newInterval)
                return res + intervals[i:]

            if newInterval[0] > curr[1]:
                res.append(curr)
            else:
                newInterval = [min(newInterval[0], curr[0]), max(newInterval[1], curr[1])]
        
        res.append(newInterval)
        return res
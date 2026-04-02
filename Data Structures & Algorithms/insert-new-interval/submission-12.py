class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find when new start is smaller
        # insert and keep extending till end is smaller than next start
        n = len(intervals)
        l, r = 0, n
        res =[]
        while l < r:
            m = l + (r - l)//2
            if intervals[m][1] < newInterval[0]:
                l = m + 1
            else:
                r = m

        for i in range(l):
            res.append(intervals[i])
        
        while l < n and newInterval[1] >= intervals[l][0]:
            newInterval[0] = min(newInterval[0], intervals[l][0])
            newInterval[1] = max(newInterval[1], intervals[l][1])
            l += 1
        res.append(newInterval)
        res += intervals[l:]
        return res


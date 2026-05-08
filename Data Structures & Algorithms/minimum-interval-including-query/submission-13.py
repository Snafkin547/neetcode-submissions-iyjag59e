class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Iterate queries in sorted order
        # Use map for result and sorted in for loop statement, so origonal persists
        # push intervals as long as start <= q into a heap
        # remove if end < q
        # first elem if exists is the minimum size
        intervals.sort()
        minQ = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minQ, (r - l + 1, r))
                i += 1
            
            while minQ and minQ[0][1] < q:
                heapq.heappop(minQ)
            res[q] = minQ[0][0] if minQ else -1
        return [res[q] for q in queries]
                
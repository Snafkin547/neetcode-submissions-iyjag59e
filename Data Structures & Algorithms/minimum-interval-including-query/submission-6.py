class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Build _intervals (end, start)
        _intervals = []
        for s, e in intervals:
            heapq.heappush(_intervals, (e, s))

        # Build minQ (val, index)
        minQ = []
        for idx, val in enumerate(queries):
            heapq.heappush(minQ, (val, idx))
        
        res = [-1] * len(queries)
        while minQ and _intervals:
            curr, idx = minQ[0]
            
            # Remove impossible intervals right_i < curr, never used
            while _intervals and curr > _intervals[0][0]:
                heapq.heappop(_intervals)
            
            # Find Smallest: Do till curr < left_i/
            temp = []
            smallest = -1
            while _intervals:
                e, s = heapq.heappop(_intervals)
                if s <= curr <= e:
                    size = e - s + 1
                    smallest = size if smallest == -1 else min(smallest, size)    
                temp.append((e, s))
            
            # Register
            res[idx] = smallest
            
            # Record the same result for same vals
            while minQ and curr == minQ[0][0]:
                curr, idx = heapq.heappop(minQ)
                res[idx] = smallest
            
            # Reinstate used intervals, as subsequent vals could fall into these ranges
            for e, s in temp:
                heapq.heappush(_intervals, (e, s))
        return res

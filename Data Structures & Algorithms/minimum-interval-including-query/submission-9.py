class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        # Heapify intervals
        heapq.heapify(intervals)
            
        # Build minQ (val, index)
        minQ = []
        for idx, val in enumerate(queries):
            heapq.heappush(minQ, (val, idx))
        
        res = [-1] * len(queries)
        q = deque()
        while minQ and (q or intervals):
            curr, idx = heapq.heappop(minQ)
            
            # Append to q till curr is smaller than any remaining start
            while intervals and intervals[0][0] <= curr:
                q.append(heapq.heappop(intervals))

            # Execute, and append back if necessary
            n = len(q)
            for i in range(n):
                s, e = q.popleft()
                if s <= curr <= e:
                    size = e - s + 1
                    res[idx] = size if res[idx] == -1 else min(res[idx], size)
                if minQ and minQ[0][0] <= e:
                    q.append((s, e))

        return res

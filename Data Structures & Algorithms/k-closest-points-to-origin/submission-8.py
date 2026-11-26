import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def dist(x,y):
            return math.sqrt(x**2 + y**2)
        
        # Compute all dist to O and save in a tuple (dist, x, y)
        # heappush
        # trim if > k
        # return the heapified res
        res = []
        for x, y in points:
            heapq.heappush(res, (-dist(x, y), x, y))
            if len(res) > k:
               heapq.heappop(res) 
        return [[x, y] for _, x, y in res]

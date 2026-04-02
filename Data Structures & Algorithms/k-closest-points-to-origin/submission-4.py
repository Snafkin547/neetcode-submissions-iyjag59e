import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        ''' 
        1) Make A
        # map{dist: list of points}
        # A list of negative distance
        # A heap from the list
        2) Pop furthest if len > k
        3) Return the list of k
        '''
        dists = [] # Keep only distance
        for x, y in points:
            dis = - (x*x + y*y)
            heapq.heappush(dists, (dis, [x, y]))
            if len(dists) > k: # Remove to be unused items
                heapq.heappop(dists)
        return [point for (dist, point) in dists]
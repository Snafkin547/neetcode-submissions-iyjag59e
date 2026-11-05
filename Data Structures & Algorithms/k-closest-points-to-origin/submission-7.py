class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [] # dist, coord
        def Edis(x, y):
            return x ** 2 + y ** 2
        # Compute all
        for x, y in points:
            heapq.heappush(minHeap, (Edis(x, y), [x, y]))
        res = []
        for i in range(k):
            _, coord = heapq.heappop(minHeap)
            res.append(coord)

        return res

        
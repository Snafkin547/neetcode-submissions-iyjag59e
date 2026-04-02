class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) < k:
            return []

        _points = [((x**2 + y**2), x, y) for x, y in points]
        heapq.heapify(_points)
        res = []
        for i in range(k):
            _, x, y = heapq.heappop(_points)
            res.append([x, y])
        return res
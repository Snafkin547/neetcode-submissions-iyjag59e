import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Heapify
        _map = defaultdict(list)
        dist = []
        for p in points:
            sq = p[0]**2 + p[1]**2
            _map[sq].append(p)
            dist.append(sq)

        heapq.heapify(dist)

        # Pop k times
        res = []
        while dist and len(res) < k:
            d = heapq.heappop(dist)
            for p in _map[d]:
                if len(res) < k:
                    res.append(p)
                else:
                    break
        return res
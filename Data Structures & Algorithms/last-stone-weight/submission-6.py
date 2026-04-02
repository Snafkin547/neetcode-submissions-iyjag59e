import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            one, two = heapq.heappop(heap), heapq.heappop(heap)
            res = one - two
            if res != 0:
                heapq.heappush(heap, res)
        return -heap[0] if heap else 0
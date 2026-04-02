import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap =[]
        for n in nums:
            heapq.heappush(maxHeap, -n)
        res = []
        for i in range(k - 1):
            heapq.heappop(maxHeap)
        return -heapq.heappop(maxHeap)



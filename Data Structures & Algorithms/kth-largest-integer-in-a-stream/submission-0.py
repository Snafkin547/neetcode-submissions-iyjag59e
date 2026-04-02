class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        self.trim()

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        self.trim()
        return self.minHeap[0]

    def trim(self):
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

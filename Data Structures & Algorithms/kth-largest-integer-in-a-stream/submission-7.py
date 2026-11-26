class KthLargest:
    # maxHeap
    # trim to k
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        self.vals = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.vals, val)
        while len(self.vals) > self.k:
            heapq.heappop(self.vals)
        return self.vals[0]
        
        

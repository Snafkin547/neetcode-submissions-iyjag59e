class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums = [-x for x in nums]
        self.nums = nums
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, - val)
        temp = []
        for i in range(self.k):
            temp.append(heapq.heappop(self.nums))

        for t in temp:
            heapq.heappush(self.nums, t)
        return - temp[-1]
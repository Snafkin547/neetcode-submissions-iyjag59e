class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        n = None
        while k > 0 and nums:
            n = heapq.heappop(nums)
            k -= 1
        return -n
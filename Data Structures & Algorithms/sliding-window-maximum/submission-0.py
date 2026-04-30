class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Keep track of best in a heapq (val, idx)
        # Ignore if idx is out of bounds
        maxH = []
        n = len(nums)
        res = []
        for i in range(n):
            heapq.heappush(maxH, (-nums[i], i))
            if i - k + 1 < 0:
                continue

            while maxH[0][1] < i - k + 1:
                heapq.heappop(maxH)
            res.append(-maxH[0][0])
        return res
                
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k most frequent elements: heap and pop k
        mp = Counter(nums)
        maxH = []
        for val, count in mp.items():
            heapq.heappush(maxH, (-count, val))
        
        res = []
        for i in range(k):
            freq, val = heapq.heappop(maxH)
            res.append(val)
        return res
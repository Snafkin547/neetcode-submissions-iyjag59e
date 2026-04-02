class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for n in nums:
            mp[n] -= 1
        minHeap =[]
        for key, v in mp.items():
            heapq.heappush(minHeap, (v, key))
        res = []
        for i in range(k):
            _, tmp = heapq.heappop(minHeap)
            res.append(tmp)
        return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k most frequent elements: heap and pop k
        mp = Counter(nums)
        freq = [[] for i in range(len(nums) +1)]
        for val, count in mp.items():
            freq[count].append(val)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

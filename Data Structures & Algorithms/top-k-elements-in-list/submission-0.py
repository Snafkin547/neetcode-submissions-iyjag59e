class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Make a frequency table
        freq = {}
        for n in nums:
            freq[n] = freq.get(n,0) + 1

        # Make a list of lists consisting of same frequency
        arr = [[] for i in range(len(nums) + 1)]
        for c, cnt in freq.items():
            arr[cnt].append(c)

        # Extract from the greatest frequencies
        res = []
        for i in range(len(arr)-1, -1, -1):
            for l in arr[i]:
                res.append(l)
                if len(res) == k:
                    return res

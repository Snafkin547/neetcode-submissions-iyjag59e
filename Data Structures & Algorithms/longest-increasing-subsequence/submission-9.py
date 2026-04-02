from bisect import bisect_left
class SegmentTree:
    def __init__(self, N):
        self.n = N
        while (self.n & (self.n - 1)) != 0:
            self.n += 1
        self.tree = [0] * (2 * self.n)

    
    def update(self, i, val):
        self.tree[i + self.n] = val
        j = (i + self.n) >> 1
        while j > 0:
            self.tree[j] = max(self.tree[j << 1], self.tree[j << 1 | 1])
            j >>= 1        

    def query(self, l, r):
        if l > r:
            return 0
        l += self.n
        r += self.n + 1
        LIS = 0
        while l < r:
            if l & 1: # If ODD = ??
               LIS = max(LIS, self.tree[l])
               l += 1
            if r & 1: # If ODD = Out of bounds
               r -= 1
               LIS = max(LIS, self.tree[r])
            l >>= 1
            r >>= 1
        return LIS               

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def compress(arr):
            sortedArr = sorted(set(arr))
            res = []
            for n in nums:
                res.append(bisect_left(sortedArr, n))
            return res
        
        compressed = compress(nums)
        LIS = 0
        st = SegmentTree(len(compressed))
        for n in compressed:
            currLIS = st.query(0, n - 1) + 1 
            st.update(n, currLIS)
            LIS = max(LIS, currLIS)
        return LIS
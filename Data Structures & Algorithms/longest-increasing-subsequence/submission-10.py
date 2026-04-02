from bisect import bisect_left
class SegmentTree:
    def __init__(self, N):
        self.n = N
        while (self.n & (self.n -1) != 0):
            self.n += 1
        self.tree = [0] * 2 * self.n
    
    def query(self, l, r) -> int:
        if l > r:
            return 0
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l & 1 == 1:
                res = max(res, self.tree[l])
                l += 1
            if r & 1 == 1:
                r -= 1
                res = max(res, self.tree[r])
                
            l >>= 1
            r >>= 1
        return res
    
    def update(self, idx, val) -> None:
        self.tree[self.n + idx] = val
        j = (self.n + idx) >> 1
        while j > 0:
            self.tree[j] = max(self.tree[j << 1], self.tree[j << 1 | 1])
            j >>= 1

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def compress(arr) -> List[int]:
            indexed = []
            newArr = sorted(set(nums))
            for n in nums:
                indexed.append(bisect_left(newArr, n))
            return indexed
        
        # loop over compressed
        compressed = compress(nums)
        LIS = 0
        st = SegmentTree(len(nums))

        # query LIS so far & update the tree
        for n in compressed:
            currLIS = st.query(0, n) + 1 # Adding sofar + this one
            LIS = max(LIS, currLIS)
            st.update(n, currLIS)
        return LIS
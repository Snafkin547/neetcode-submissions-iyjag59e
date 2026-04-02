class SegmentTree:
    def __init__(self, n):
        self.n = n
        while self.n & (self.n - 1)!= 0:
            self.n += 1
        self.tree = [0] * (2 * self.n)
    def query(self, l, r):
        if l > r:
            return 0
        l += self.n
        r += self.n
        res = 0
        while l < r:
            if l & 1: # If odd = 
                res = max(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res
    
    def update(self, idx, val):
        self.tree[idx + self.n] = val
        j = (idx + self.n) >> 1
        while j > 0:
            self.tree[j] = max(self.tree[j << 1], self.tree[j << 1 | 1])
            j >>= 1
                

class Solution:
    def bisec_left(self, arr, n):
        l, r = 0, len(arr)
        while l < r: # Wanna find an index, possibly at 0 or len(arr)
            mid = l + ((r - l) >> 1)
            if arr[mid] < n:
                l = mid + 1
            else:
                r = mid
        return r

    def lengthOfLIS(self, nums: List[int]) -> int:
        def compress(arr):
            ordered = []
            newArr = sorted(set(arr))
            for n in nums:
                ordered.append(self.bisec_left(newArr, n))
            return ordered
        
        nums = compress(nums)
        LIS = 0
        st = SegmentTree(len(nums))
        for n in nums:
            currLIS = st.query(0, n) + 1
            LIS = max(LIS, currLIS)
            st.update(n, currLIS)
        return LIS
            
        
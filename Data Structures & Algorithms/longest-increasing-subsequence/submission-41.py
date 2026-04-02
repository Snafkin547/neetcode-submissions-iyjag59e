class segment_tree:
    def __init__(self, N):
        self.n = N
        # Make a closest but greater power of 2
        while self.n & (self.n - 1):
            self.n += 1
        self.arr = [0] * self.n * 2
    
    def update(self, val, idx):
        i = idx + self.n
        self.arr[i] = val
        i >>= 1

        while i >= 1:
            self.arr[i] = (max(self.arr[i<< 1], self.arr[i<< 1|1]))
            i >>= 1
    
    def query(self, l, r):
        if l > r:
            return 0
        l += self.n
        r += self.n # Inclusive
        res = float('-inf')
        while l <= r:
            if l & 1:
                res = max(res, self.arr[l])
                l += 1
            if not (r & 1):
                res = max(res, self.arr[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # State index, prev
        # Ops, include this or not
        # Build a LIS by finding leftmost index of the curr val
        def find_idx(val, s):
            l, r = 0, len(s)
            while l < r:
                m = l + ((r - l) >> 1)
                if s[m] < val:
                    l = m + 1
                else:
                    r = m
            return l
        def order(arr):
            s = sorted(set(arr))
            ordered = []
            for n in arr:
                i = find_idx(n, s)
                ordered.append(i)
            return ordered

        nums = order(nums)
        n = len(nums)
        st = segment_tree(n)
        LIS = 0

        for o in nums:
            curLIS = st.query(0, o - 1) + 1
            st.update(curLIS, o)
            LIS = max(curLIS, LIS)
        return LIS
class segT:
    def __init__(self, N):
        self.n = N
        while self.n & (self.n - 1)!=0:
            self.n += 1
        self.tree = [0] * (self.n * 2)
    
    def query(self, l, r):
        l += self.n
        r += self.n
        res = 0
        while l <= r:
            # l is odd = right leaf, evaluate as it is and dont check its parent as we cannnot include l - 1, whcih shares the same prent
            if l&1:
                res = max(res, self.tree[l])
                l += 1
            # r is even = left leaf, we cannot include right leaf due to boundary
            if not (r&1):
                res = max(res, self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res

    def update(self, i, val):
        self.tree[self.n + i] = val
        j = (self.n + i) >> 1
        while j >= 1:
            self.tree[j] = max(self.tree[j << 1], self.tree[j << 1|1])
            j >>= 1


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def leftsec(s, val):
            l, r = 0, len(s)
            while l < r:
                m = l + ((r - l)>>1)
                if s[m] < val:
                    l = m + 1
                else:
                    r = m
            return l

        def compress(arr):
            s = sorted(set(arr))
            ordered = []
            for n in arr:
                ordered.append(leftsec(s, n))
            return ordered
        
        order = compress(nums)
        st = segT(len(order))
        LIS = 0
        for val in order:
            curr = st.query(0, val - 1) + 1
            st.update(val, curr)
            LIS = max(LIS, curr)
        return LIS
        
        
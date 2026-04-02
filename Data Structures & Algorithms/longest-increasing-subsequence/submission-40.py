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

        LIS = []
        for v in nums:
            if not LIS or v > LIS[-1]:
                LIS.append(v)
            else:
                LIS[find_idx(v, LIS)] = v
        return len(LIS)

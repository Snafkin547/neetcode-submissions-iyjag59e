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
        compressed = compress(nums)
        dp = [compressed[0]]
        LIS = 1
        for i, n in enumerate(compressed):
            if dp[-1] < n:
                dp.append(n)
                LIS += 1
                continue
            idx = self.bisec_left(dp, n)
            dp[idx] = n

        return LIS

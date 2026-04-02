from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]
        LIS = 1
        for i, n in enumerate(nums):
            # Increase LIS only if greater than last elem
            if dp[-1] < n:
                dp.append(n)
                LIS += 1
            # Otherwise, update current arr, so subsequently it'represents possible array with the element in that index
            else:
                idx = bisect_left(dp, n)
                dp[idx] = n
        return LIS
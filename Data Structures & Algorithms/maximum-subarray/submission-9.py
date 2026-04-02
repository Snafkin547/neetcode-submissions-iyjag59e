class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = float('-inf')
        curr = 0
        for r in range(n):
            curr += nums[r]
            res = max(res, curr)
            if curr < 0:
                curr = 0
        return res
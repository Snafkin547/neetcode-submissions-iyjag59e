class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        n = len(nums)
        res = float('-inf')
        prefix = suffix = 0
        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - i - 1] * (suffix or 1)
            res = max(res, max(prefix, suffix))
        return res


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        n = len(nums)
        res = float('-inf')
        curr = 0
        for i in range(n):
            curr = nums[i] * (curr or 1)
            res = max(res, curr)
        
        curr = 1
        for i in range(n - 1, -1, -1):
            curr = nums[i] * (curr or 1)
            res = max(res, curr)
        return res


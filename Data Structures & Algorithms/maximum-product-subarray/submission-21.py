class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Split array between zeros
        # Count negs: Address cases Odd/Even
        res = max(nums)
        prod = 1
        for n in nums:
            prod *= n
            res = max(res, prod)
            if n == 0:
                prod = 1
        prod = 1
        for n in reversed(nums):
            prod *= n
            res = max(res, prod)
            if n == 0:
                prod = 1
        return res

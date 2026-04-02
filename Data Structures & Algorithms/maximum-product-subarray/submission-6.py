class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def calc(l, end):
            res = 1
            for elm in nums[l : end]:
                res *= elm
            print(nums[l: end], res)
            return res

        # From where to where = Where to start and where to end
        n = len(nums)
        res =  -float('inf')
        for size in range(1, n + 1):
            for l in range(n - size + 1):
                prod = calc(l, l + size)
                res = max(res, prod)
        return res
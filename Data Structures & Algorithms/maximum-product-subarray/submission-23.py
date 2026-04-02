class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Brute Force
        '''
        Move index one by one and extend size to check if best
        Time: O(n^2)
        Memory: O(n)
        '''
        res = max(nums)
        for l in range(len(nums)):
            prod = nums[l]
            res = max(res, prod)
            for j in range(l + 1, len(nums)):
                prod *= nums[j]
                res = max(res, prod)
        return res

            
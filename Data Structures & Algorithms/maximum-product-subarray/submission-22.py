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
            for r in range(l + 1, len(nums) + 1):
                prod = 1
                for n in nums[l:r]:
                    prod*=n
                res = max(res, prod)
        return res

            
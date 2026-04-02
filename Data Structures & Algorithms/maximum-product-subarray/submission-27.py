class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        '''
        Two passes left to right, restart the state if encounter zero
        Time: O(n)
        Memory: O(1)
        '''
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
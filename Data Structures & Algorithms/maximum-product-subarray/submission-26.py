class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        '''
        Keep min and max, min * neg val might produce new maximum
        As n is always multiplied, wrongly identifying max/min despite 0 is avoided
        Time: O(n)
        Memory: O(1)
        '''
        res = max(nums)
        curMin, curMax =1, 1
        
        for n in nums:
            sofar = n * curMax
            curMax = max(n, sofar, n * curMin)
            curMin = min(n, sofar, n * curMin)
            res = max(res, curMax)
        return res
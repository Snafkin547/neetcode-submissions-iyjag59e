class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [1]*n, [1]*n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        res = []
        for i in range(n):
            res.append(prefix[i] * suffix[i])
        return res
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total%2:
            return False
        target = 1 << (total//2)
        res = 1 << 0
        for val in nums:
            res |= res << val
        return (target & res)!= 0
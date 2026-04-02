class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        if l % 2 == 0:
            ttl = (1 + l) * (l//2)
        else:
            ttl = (1 + l) * (l//2) + (l+1)//2
        return ttl - sum(nums)

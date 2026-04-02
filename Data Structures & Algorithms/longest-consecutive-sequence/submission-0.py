class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxCount = 0
        for n in nums:
            curr = 0
            k = n
            while k in numSet:
                curr += 1
                k += 1
            maxCount = max(maxCount,curr)
        return maxCount
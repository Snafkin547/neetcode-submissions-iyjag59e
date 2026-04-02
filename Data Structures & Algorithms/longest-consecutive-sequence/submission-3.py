class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        maxCount = 1
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                curr+=1
                maxCount = max(maxCount, curr)
            elif nums[i] == nums[i-1]:
                continue
            else:
                curr = 1
        return maxCount
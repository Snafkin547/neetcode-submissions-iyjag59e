class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sofar = nums[0]
        for i in range(len(nums)):
            curr = nums[i]
            sofar = max(sofar, curr)
            for j in range(i + 1, len(nums)):
                curr *= nums[j]
                sofar = max(sofar, curr)
        return sofar
            
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        nums[1] = max(nums[:2])
        for i in range(2, n):
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
        print(nums)
        return nums[-1]
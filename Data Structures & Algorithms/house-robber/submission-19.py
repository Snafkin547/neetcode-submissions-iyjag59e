class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)

        # Decide whether to rob or keep i - 1 total
        prev, curr = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            prev, curr = curr, max(curr, prev + nums[i])
        return curr
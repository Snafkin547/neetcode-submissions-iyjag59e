# DP bottom up
# Optimal
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        def helper(start, end):

            prev = curr = 0

            for i in range(start, end):
                temp = max(curr, prev + nums[i])
                prev = curr
                curr = temp
            return curr

        return max(helper(0, len(nums) -1), helper(1, len(nums)))
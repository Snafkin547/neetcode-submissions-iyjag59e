# DP bottom up
# Optimal
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            n = len(arr)
            if n == 1:
                return arr[0]

            prev, curr = arr[0], max(arr[0], arr[1])

            for i in range(2, n):
                temp = max(curr, prev + arr[i])
                prev = curr
                curr = temp
            return curr

        return max(helper(nums[1:]), helper(nums[:-1]))
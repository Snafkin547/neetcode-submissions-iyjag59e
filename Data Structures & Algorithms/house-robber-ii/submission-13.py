# DP bottom up
# Optimal
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n <= 3:
            return max(nums)

        res = 0
        dp = [0] * (n - 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        res = dp[-1]

        dp[0] = nums[1]
        dp[1] = max(nums[1], nums[2])
        for i in range(3, n):
            dp[i - 1] = max(dp[i - 2], dp[i - 3] + nums[i])
        return max(res, dp[-1])
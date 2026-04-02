# DP bottom up
# Optimal
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n <= 3:
            return max(nums)

        dp = [[-1] * 2 for _ in range(n)]
        start0 = True
        dp[0][start0] = nums[0]
        dp[1][start0] = max(nums[0], nums[1])
        for i in range(2, n - 1):
            dp[i][start0] = max(dp[i - 1][start0], dp[i - 2][start0] + nums[i])
        
        start0 = False
        dp[1][start0] = nums[1]
        dp[2][start0] = max(nums[1], nums[2])
        for i in range(3, n):
            dp[i][start0] = max(dp[i - 1][start0], dp[i - 2][start0] + nums[i])
        return max(dp[-2][True], dp[-1][False])
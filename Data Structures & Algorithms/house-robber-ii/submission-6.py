# DP bottom up
# DP top down
# Optimal
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [[-1] * 2 for _ in range(n)]
        
        def dfs(i, isFirst):
            if (isFirst and i >= n - 1) or (not isFirst and i >= n):
                return 0
            
            if dp[i][isFirst] != -1:
                return dp[i][isFirst]
            
            dp[i][isFirst] = max(dfs(i + 1, isFirst), nums[i] + dfs(i + 2, isFirst))
            return dp[i][isFirst]
        return max(dfs(0, True), dfs(1, False))
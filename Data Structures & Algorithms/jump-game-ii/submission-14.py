#DP Bottom Up
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [10001] * n
        dp[0] = 0
        
        for i in range(n):
            end = min(i + nums[i] + 1, n)
            for j in range(i + 1, end):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]
                

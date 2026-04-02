class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True
        for i in range(n - 2, -1, -1):
            end = min(i + nums[i] + 1, n)
            for j in range(i + 1, end):
                if dp[j]:
                    dp[i] = True
        return dp[0]

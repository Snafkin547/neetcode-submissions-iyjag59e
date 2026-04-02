class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # State index, prev
        # Ops, include this or not
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(i, -1, -1):
                if j == 0 or nums[i] > nums[j - 1]: # j needs to be at most i - 1 to make a meaningful comparison
                    dp[i][j] = max(dp[i + 1][j], 1 + dp[i + 1][i + 1])
                else:
                    dp[i][j] = dp[i + 1][j]
        return dp[0][0]
                    
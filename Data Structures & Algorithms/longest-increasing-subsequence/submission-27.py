class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # State index, prev
        # Ops, include this or not
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for prev in range(i):
                # Exclude curr
                dp[i][prev] = max(dp[i][prev], dp[i - 1][prev])
                # Include curr if greater
                if prev == 0 or nums[prev - 1] < nums[i - 1]:
                    dp[i][i] = max(dp[i][i], 1 + dp[i - 1][prev])
        return max(dp[-1])
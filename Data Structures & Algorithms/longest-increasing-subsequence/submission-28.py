class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # State index, prev
        # Ops, include this or not
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        # dp[curr][end] = LIS till curr thats ending at end
        # So curr - 1 is the at least length for the current end if not longer
        for curr in range(1, n + 1):
            for end in range(curr):
                dp[curr][end] = dp[curr - 1][end]
                if end == 0 or nums[curr - 1] > nums[end - 1]:
                    dp[curr][curr] = max(dp[curr][curr], 1 + dp[curr - 1][end])
        return max(dp[-1])
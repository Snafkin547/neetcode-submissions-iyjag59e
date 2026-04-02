class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # State index, prev
        # Ops, include this or not

        # Can we extend nums[i] if nums[j] is the prev and does it make the longest?
        # i & j both 1-indexed, so that 0 represents no prev

        n = len(nums)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(i + 1):
                if j == 0 or nums[j - 1] < nums[i - 1]:
                    # Updating with nums[i] means, the subsequent LIS would reference i as prev
                    # Therefore, we challenge the existing dp[i]
                    dp[i] = max(dp[i], 1 + dp[j])
        # The final row represents each LIS if the val in a index is prev for the last i
        # Take the max of them
        return max(dp)

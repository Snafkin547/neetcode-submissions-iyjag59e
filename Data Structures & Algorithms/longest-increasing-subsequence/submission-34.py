class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # State index, prev
        # Ops, include this or not

        # Can we extend nums[i] if nums[j] is the prev and does it make the longest?
        # i & j both 1-indexed, so that 0 represents no prev

        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i):
                dp[i][j] = dp[i - 1][j] # Inherit from the previous iteration
                if j == 0 or nums[j - 1] < nums[i - 1]:
                    # Updating with nums[i] means, the subsequent LIS would reference i as prev
                    # Therefore, we challenge the existing dp[i][i]
                    dp[i][i] = max(dp[i][i], 1 + dp[i][j])
        # The final row represents each LIS if the val in a index is prev for the last i
        # Take the max of them
        return max(dp[-1])

#   [9,1,4,2,3,3,7]
# [1,0,0,0,0,0,0,0]
# [0,1,0,0,0,0,0,0]
# [0,0,0,0,0,0,0,0]

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # State index, prev
        # Ops, include this or not

        # Can we extend nums[i] if nums[j] is the prev and does it make the longest?
        # i is 0-indexed but j is 1-indexed, so that j = 0 represents no prev

        n = len(nums)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            for j in range(i, -1, -1):
                if j == 0 or nums[j - 1] < nums[i]:
                    # Updating with nums[i] means, the subsequent LIS would reference i as prev
                    # Therefore, we challenge the existing dp[j] by adding 1 to dp[i + 1], which keeps increasing as it is being last elem
                    dp[j] = max(dp[j], 1 + dp[i + 1])
            print(dp)
        return dp[0]

#   [9,1,4,2,3,3,7]
# [0,0,1,1,1,1,1,0]
# [0,0,2,1,2,1,1,0]
# [0,0,2,1,2,1,1,0]
# [0,0,2,1,2,1,1,0]
# [0,0,2,1,2,1,1,0]
# [0,0,3,1,2,1,1,0]
# [4,0,3,1,2,1,1,0]
# [4,0,3,1,2,1,1,0]
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # State index, prev
        # Ops, include this or not
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1):
                if j == 0 or nums[j - 1] < nums[i]:
                    dp[i][j] = max(dp[i + 1][j], 1 + dp[i + 1][i + 1])
                else:
                    dp[i][j] = dp[i + 1][j]
    
        return dp[0][0]

#   [9,1,4,2,3,3,7]
# [0,0,0,0,0,0,0,0]
# [1,0,1,1,1,1,1,0]
# [2,0,2,1,2,1,0,0]
# [2,0,2,1,2,0,0,0]
# [3,0,3,1,0,0,0,0]
# [3,0,3,0,0,0,0,0]
# [4,0,0,0,0,0,0,0]
# [4,0,0,0,0,0,0,0]
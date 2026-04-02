class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Make a binary decision
        # Memoization
        n = len(nums)
        dp = [-1] * n
        def dfs(idx, curr):
            if idx == n:
                return 0
                
            if dp[curr] != -1:
                return dp[curr]

            LIS = dfs(idx + 1, curr)
            if curr == -1 or nums[curr] < nums[idx]:
                LIS = max(dfs(idx + 1, idx) + 1, LIS)
            dp[curr] = LIS
            return LIS
 
        return dfs(0, -1)
        # return max(dfs(i,  -1) for i in range(len(nums)))
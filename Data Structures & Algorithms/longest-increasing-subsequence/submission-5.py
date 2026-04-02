class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Make a binary decision
        # Memoization
        n = len(nums)
        dp = {}
        def dfs(idx, curr):
            if idx == n:
                return 0
                
            s = (idx, curr)
            if s in dp:
                return dp[s]

            LIS = dfs(idx + 1, curr)
            if curr == -1 or nums[curr] < nums[idx]:
                LIS = max(dfs(idx + 1, idx) + 1, LIS)
            dp[s] = LIS
            return LIS
 
        return dfs(0,  -1)
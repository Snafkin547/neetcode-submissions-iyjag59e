class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Make a binary decision
        # Memoization
        n = len(nums)
        dp = [-1] * n
        def dfs(idx):                
            if dp[idx] != -1:
                return dp[idx]

            LIS = 1
            for j in range(idx + 1, n):
                if nums[idx] < nums[j]:
                    LIS = max(dfs(j) + 1, LIS)
            dp[idx] = LIS
            return LIS
 
        return max(dfs(i) for i in range(n))
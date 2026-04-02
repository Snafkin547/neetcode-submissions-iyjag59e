class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [-1] * n
        def dfs(i):
            if i == n:
                return 0
            if dp[i]!= -1:
                return dp[i]
            dp[i] = 1
            for k in range(i + 1, n):
                if nums[i] < nums[k]:
                   dp[i] = max(dp[i], 1 + dfs(k))
            return dp[i]
        res = 0
        for i in range(n):
            res = max(res, dfs(i))
        return res
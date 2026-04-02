class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ttl = sum(nums)
        if ttl%2:
            return False
        
        target = ttl >> 1
        n = len(nums)
        dp = [False] * (1+target)

        def dfs(i, balance):
            if balance == 0:
                return True

            if dp[balance]:
                return dp[balance]

            for k in range(i, n):
                if balance - nums[k] >= 0:
                    dp[balance]|= dfs(k + 1, balance - nums[k])
            return dp[balance]
        return dfs(0, target)

            
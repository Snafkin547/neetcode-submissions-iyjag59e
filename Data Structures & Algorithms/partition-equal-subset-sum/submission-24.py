class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ttl = sum(nums)
        if ttl%2:
            return False
        
        target = ttl >> 1
        n = len(nums)
        dp = [None] * (1+target)

        def dfs(i, balance):
            if balance == 0:
                return True

            if dp[balance]!=None:
                return dp[balance]

            res = False
            for k in range(i, n):
                if balance - nums[k] >= 0:
                    res|= dfs(k + 1, balance - nums[k])
            dp[balance] = res
            return dp[balance]
        return dfs(0, target)

            
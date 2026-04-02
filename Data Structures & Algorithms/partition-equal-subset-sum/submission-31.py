class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ttl = sum(nums)
        if ttl%2:
            return False
        target = ttl >> 1
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(target, num-1,-1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[-1]

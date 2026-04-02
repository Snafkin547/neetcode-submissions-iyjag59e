class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ttl = sum(nums)
        if ttl%2:
            return False
        target = ttl >> 1
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(len(dp)-1, -1,-1):
                if dp[i] and i + num <= target:
                    dp[i + num] = True
        print(dp)
        return dp[-1]

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total%2:
            return False
        target = total//2
        dp = [False] * (target + 1)
        dp[0] = True # 0 is always possible
        
        for val in nums:
            for t in range(target, - 1, -1):
                if t - val >= 0:
                   dp[t] |= dp[t - val]
        return dp[-1]
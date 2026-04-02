class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total < abs(target) or (target + total)%2:
            return 0

        subset = (total + target)//2
        dp = [0] * (subset + 1)
        dp[0] = 1
        for n in nums:
            for i in range(subset, n -1,-1):
                dp[i] += dp[i - n]
        return dp[subset]
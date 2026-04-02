class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        res = sum(nums)
        if res != (res >> 1)<<1:
            return False
        res >>= 1
        dp = [False] * (res + 1)
        dp[0] = True
        for n in nums:
            for i in range(res, n - 1, -1):
                dp[i] = dp[i - n] | dp[i]
        return dp[res]        
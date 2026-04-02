class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        res = sum(nums)
        if res != (res >> 1) << 1:
            return False
        res >>= 1
        dp = [False] * (res + 1)
        nextdp = [False] * (res + 1)
        dp[0] = True
        for n in nums:
            for i in range(1, res + 1):
                if i >= n:
                    nextdp[i] = dp[i - n] | dp[i]
                else:
                    nextdp[i] = dp[i]
            dp, nextdp = nextdp, dp
        return dp[res]
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # state i balance
        # ops + -
        dp = defaultdict(int)
        dp[0] = 1

        for n in nums:
            temp = defaultdict(int)
            for i in dp.keys():
               temp[i + n] += dp[i]
               temp[i - n] += dp[i]
            dp = temp
        return dp[target]
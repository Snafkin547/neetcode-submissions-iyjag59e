class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def helper(i, balance):
            if i == n:
                return balance == 0
            if (i, balance) in dp:
                return dp[(i, balance)]
            
            dp[(i, balance)] = helper(i + 1, balance + nums[i]) + helper(i + 1, balance - nums[i])
            return dp[(i, balance)]
        return helper(0, target)
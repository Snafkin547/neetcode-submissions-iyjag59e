class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)
        def helper(i, balance):
            # State: i, balance
            # Ops: + and -
            if i == n and balance == 0:
                return 1
            if i >= n:
                return 0
            if (i, balance) in dp:
                return dp[(i, balance)]
            
            # Plus
            dp[(i, balance)] += helper(i + 1, balance - nums[i])
            # Minus
            dp[(i, balance)] += helper(i + 1, balance + nums[i])

            return dp[(i, balance)]
        return helper(0, target)
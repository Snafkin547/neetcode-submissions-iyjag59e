class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # State: number, balance
        n = len(nums)
        dp = defaultdict(int)
        dp[0] = 1
        for i in range(n):
            temp = defaultdict(int)
            for ttl, count in dp.items():
                temp[ttl + nums[i]] += count
                temp[ttl - nums[i]] += count
            dp = temp
        return dp[target]

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # State: number, balance
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(n):
            for ttl, count in dp[i].items():
                dp[i + 1][ttl + nums[i]] += count
                dp[i + 1][ttl - nums[i]] += count
        return dp[n][target]

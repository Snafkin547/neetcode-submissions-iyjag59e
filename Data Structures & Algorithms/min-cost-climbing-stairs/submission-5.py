class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # State: Min cost at i-th
        # Ops: +1 or +2 floors ahead
        # Catch: Start from both 0 and 1
        n = len(cost)
        if n <= 2:
            return min(cost)

        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2])
        return dp[-1]

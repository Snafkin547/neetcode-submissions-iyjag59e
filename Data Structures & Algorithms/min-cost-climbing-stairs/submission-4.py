class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # State: Min cost at i-th
        # Ops: +1 or +2 floors ahead
        # Catch: Start from both 0 and 1
        n = len(cost)
        dp = [-1] * n
        def pay_to_climb(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = cost[i] + min(pay_to_climb(i + 1), pay_to_climb(i + 2))
            return dp[i]
        return min(pay_to_climb(0), pay_to_climb(1))

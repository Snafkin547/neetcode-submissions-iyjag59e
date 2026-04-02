class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # State: Min cost at i-th
        # Ops: +1 or +2 floors ahead
        # Catch: Start from both 0 and 1
        n = len(cost)
        for i in range(n - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])

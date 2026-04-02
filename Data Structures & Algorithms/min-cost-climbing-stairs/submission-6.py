class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # State: Min cost at i-th
        # Ops: +1 or +2 floors ahead
        # Catch: Start from both 0 and 1
        n = len(cost)
        if n <= 2:
            return min(cost)

        prev = curr = 0
        for i in range(2, n + 1):
            temp = min(cost[i - 1] + curr, cost[i - 2] + prev)
            prev, curr = curr, temp
        return curr

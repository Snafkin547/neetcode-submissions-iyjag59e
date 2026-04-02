class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return cost[0]
        if len(cost) == 2:
            return min(cost)
        for i in range(2, len(cost)):
             cost[i] += min(cost[i-2:i])
        return min(cost[-2:])

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # sub prob: how much from here till end
        # compare i + 1 and i + 2
        n = len(cost)
        for i in range(n - 3, -1, -1):
            cost[i] = cost[i] + min(cost[i + 1], cost[i + 2]) 
        return min(cost[:2])
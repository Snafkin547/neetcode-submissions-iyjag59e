[1,2,1,2,1,1,1]
[4,5,3,3,2,1,1]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # if len(cost) == 2:
        #     return min(cost[0], cost[1])
        for idx in range(len(cost) - 3, -1, -1):
            remaining = min(cost[idx+1], cost[idx+2])
            cost[idx] += remaining
        return min(cost[0], cost[1])        
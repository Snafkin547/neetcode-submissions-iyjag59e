class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        l, r = 0, len(gas) - 1
        ttl = gas[r] - cost[r]
        while l < r:
            
            if ttl < 0:
                r -= 1
                ttl += gas[r] - cost[r]
            else:
                ttl += gas[l] - cost[l]
                l += 1
        return r
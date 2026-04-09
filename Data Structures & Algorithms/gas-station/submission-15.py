class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0 or len(gas)!= len(cost):
            return -1
        n = len(gas)
        s, e = n - 1, 0
        balance = gas[s] - cost[s]
        while s > e:
            if balance < 0:
                s -= 1
                balance += gas[s] - cost[s]
            
            else:
                balance += gas[e] - cost[e]
                e += 1
        return s if balance >= 0 else -1

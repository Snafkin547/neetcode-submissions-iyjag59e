class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0 or len(gas)!= len(cost):
            return -1
        n = len(gas)
        balance = res = 0
        for i in range(n):
            balance += gas[i] - cost[i]
            if balance < 0:
                balance = 0
                res = i + 1
        return res
                

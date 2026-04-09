class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0 or len(gas)!= len(cost):
            return -1
        n = len(gas)
        best = float('-inf')
        balance = res = 0
        for i in range(n - 1, -1, -1):
            gas[i] -= cost[i]
            balance += gas[i]
            if best < balance:
                res = i
                best = balance
        return res

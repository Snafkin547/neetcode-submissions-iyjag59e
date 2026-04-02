class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # [-1, 0, -1, 3]
        # [-1, 0, -1, 3, -1, 0, -1, 3]

        # [4, -1, -1, -1, -1, 3, -1, 4, -1, -1, -1, -1, 3, -1]
        n = len(gas)
        for i in range(n):
            gas[i] -= cost[i]
        if sum(gas) < 0:
            return -1

        gas *= 2
        cnt = steps = 0
        for i in range(len(gas)):
            if steps == n:
                return (i - steps + 1) % n
            cnt += gas[i]
            if cnt <= 0:
                steps = cnt = 0
            steps += 1
        return -1
        
        
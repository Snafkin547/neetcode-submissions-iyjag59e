class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) != len(speed):
            return -1
        earliest = float('-inf')
        arr = [(p, s) for p, s in sorted(zip(position, speed))]
        
        n = len(position)
        fleet = 0
        for i in range(n - 1, -1, -1):
            time = (target - arr[i][0])/arr[i][1]
            if time > earliest:
                fleet += 1
                earliest = time
        
        return fleet
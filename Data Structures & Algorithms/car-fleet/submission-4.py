class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        position, speed = zip(*sorted(zip(position, speed),reverse=True))

        fleetSet = set()
        maxT = [] # Keep track of latest arrival so far, to prevent bypassing
        numFleet = 0

        for i in range(len(position)):
            dist = target - position[i]
            t = dist/speed[i]
            if t not in fleetSet and (not maxT or t > maxT[-1]):
                fleetSet.add(t)
                maxT.append(t)
                numFleet += 1
        
        return numFleet
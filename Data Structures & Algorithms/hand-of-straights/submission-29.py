# Queue
# Ordered Map
# HashMap
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False

        mp = defaultdict(int)
        for h in hand:
            mp[h] += 1
        
        q = deque()
        openG, prev = 0, -1
        
        for h in sorted(mp):
            if (openG and h > prev + 1) or mp[h] < openG:
                return False
            q.append(mp[h] - openG)
            openG = mp[h]
            prev = h
            if len(q) == groupSize:
                openG -= q.popleft()
        return openG == 0

            
        
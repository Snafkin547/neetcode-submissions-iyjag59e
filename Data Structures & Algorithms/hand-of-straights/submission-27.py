# Sorting
# Queue
# Ordered Map
# HashMap
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False

        hand.sort()
        mp = defaultdict(int)
        
        for h in hand:
            mp[h] += 1
        # hand = [v for v in sorted(mp)]
        for h in hand:
            if not mp[h]:
                continue
            s = h
            for i in range(s,s+groupSize):
                if not mp[i]:
                    return False
                mp[i] -= 1
        return True

            
        
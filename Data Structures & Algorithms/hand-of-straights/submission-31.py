
# HashMap
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False

        mp = defaultdict(int)
        for h in hand:
            mp[h] += 1
        
        for h in hand:
            if not mp[h]:
                continue
            s = h
            # Find start
            while mp[s-1]:
                s -= 1
            # Consume everything up to h, otherwise you end up with finding start for every single index
            while s <= h:
                while mp[s]:
                    for i in range(s, s+ groupSize):
                        if not mp[i]:
                            return False
                        mp[i] -=1
                s += 1
        return True
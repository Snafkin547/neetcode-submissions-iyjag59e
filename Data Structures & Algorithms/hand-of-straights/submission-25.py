class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False

        mp = defaultdict(int)
        for h in hand:
            mp[h] += 1
        
        for h in hand:
            s = h
            while mp[s-1]:
                s -= 1
            while s <= h:
                while mp[s]:
                    for i in range(s, s + groupSize):
                        if not mp[i]:
                            return False
                        mp[i] -= 1
                s += 1
        return True
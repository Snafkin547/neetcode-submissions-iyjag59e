class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False

        mp = defaultdict(int)
        for h in hand:
            mp[h] += 1
        
        hand.sort()
        for h in hand:
            if mp[h]:
                for i in range(h, h + groupSize):
                    if not mp[i]:
                        return False
                    mp[i] -= 1
        return True
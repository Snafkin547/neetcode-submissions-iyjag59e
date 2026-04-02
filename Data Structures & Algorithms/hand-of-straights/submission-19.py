class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False

        mp = defaultdict(int)
        for h in hand:
            mp[h] += 1
        
        for h in hand:
            st = h
            while mp[st -1]:
                st -= 1
            while st <= h:
                while mp[st]:
                    for i in range(st, st + groupSize):
                        if not mp[i]:
                            return False
                        mp[i] -= 1
                st += 1
        return True
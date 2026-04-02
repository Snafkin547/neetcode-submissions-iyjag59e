class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        mp = defaultdict(int)
        for h in hand:
            mp[h] += 1
        while mp:
            start = min(mp)
            for i in range(start, start + groupSize):
                if i not in mp:
                    return False
                else:
                    mp[i] -= 1
                    if not mp[i]:
                        del mp[i]

        return True
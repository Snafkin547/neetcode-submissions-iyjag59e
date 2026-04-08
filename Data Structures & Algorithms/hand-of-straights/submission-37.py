class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        count = Counter(hand)
        hand.sort()
        for h in hand:
            if count[h]:
                for i in range(h, h + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True
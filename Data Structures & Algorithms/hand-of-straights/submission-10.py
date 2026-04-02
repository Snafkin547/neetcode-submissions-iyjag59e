class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        cnter = collections.Counter(hand)
        hand.sort()
        for n in hand:
            if cnter[n]:
                for i in range(n, n + groupSize):
                    if not cnter[i]:
                        return False
                    cnter[i] -= 1
            
        return True
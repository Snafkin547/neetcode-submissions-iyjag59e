class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        cnter = collections.Counter(hand)
        hand.sort()
        q = deque()
        nGroup = 0
        prev = -1

        for n in sorted(cnter):
            if (nGroup > cnter[n] or (nGroup > 0 and prev + 1 != n)):
                return False
            
            q.append(cnter[n] - nGroup)
            nGroup = cnter[n] 
            if len(q) == groupSize:
              nGroup -= q.popleft()
            prev = n
        return nGroup == 0
            
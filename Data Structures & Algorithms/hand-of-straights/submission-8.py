class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = groupSize
        if len(hand) < n or len(hand)%n!=0:
            return False
        size = int(len(hand)//n)
        hMap = collections.Counter(hand)
        
        for _ in range(size):
            cnt = 0
            prev = None
            for h in sorted(hMap):
                if prev:
                    if prev + 1 != h:
                        return False
                prev = h
                hMap[h] -= 1
                cnt += 1
                if hMap[h] <= 0:
                    del hMap[h]
                if cnt == n:
                    break

        return not hMap
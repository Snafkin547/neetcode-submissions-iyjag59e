# Heap
# HashMap
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False

        mp = defaultdict(int)
        for h in hand:
            mp[h] += 1
        
        minH = [v for v in mp]
        heapq.heapify(minH)
        while minH:
            s = minH[0]
            for i in range(s, s + groupSize):
                if not mp[i]:
                    return False
                mp[i] -= 1
                if not mp[i]:
                    if minH[0]!=i:
                        return False
                    heapq.heappop(minH)
        return True

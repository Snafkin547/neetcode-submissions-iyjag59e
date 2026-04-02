class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        mp = defaultdict(int)
        for h in hand:
            mp[h] += 1

        minH = list(mp.keys())
        heapq.heapify(minH)
        while minH:
            start = minH[0]
            for i in range(start, start + groupSize):
                if i not in mp:
                    return False
                else:
                    mp[i] -= 1
                    if mp[i] == 0:
                        if i !=minH[0]:
                            return False
                        heapq.heappop(minH)
        return True
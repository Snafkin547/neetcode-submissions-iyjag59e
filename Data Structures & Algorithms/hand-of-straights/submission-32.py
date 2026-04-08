class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False
        
        mp = defaultdict(int)
        for h in hand:
            mp[h] += 1
        
        for h in hand:
            if not mp[h]:
                continue
            k = h
            while mp[k - 1]:
                k -= 1
            for i in range(k, k + groupSize):
                if not mp[i]:
                    return False
                mp[i] -= 1
        return True

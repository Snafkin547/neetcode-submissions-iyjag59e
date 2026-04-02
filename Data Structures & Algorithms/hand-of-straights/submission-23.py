class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False

        mp = defaultdict(int)
        for h in hand:
            mp[h] += 1
        
        openG, prev = 0, -1
        q = deque()
        for st in sorted(mp):
            if openG > 0 and st > prev + 1 or openG > mp[st]:
                return False
            q.append(mp[st] - openG)
            prev = st
            openG = mp[st]
            if len(q) == groupSize:
                openG -= q.popleft()

        return openG == 0
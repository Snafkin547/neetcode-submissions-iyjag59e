class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        mp = defaultdict(int)
        for h in hand:
            mp[h] += 1

        q = deque()
        openG, prev = 0, -1
        for i in sorted(mp):
            if openG > mp[i] or (openG > 0 and i > prev + 1):
                return False
            q.append(mp[i] - openG)
            openG = mp[i]
            prev = i
            if len(q) == groupSize:
                openG -= q.popleft()
        return openG == 0
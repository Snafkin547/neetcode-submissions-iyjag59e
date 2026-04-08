class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        count = Counter(hand)
        openG = 0
        prev = -1
        q = deque()
        for num in sorted(count):
            if (openG > 0 and prev + 1 != num) or count[num] < openG:
                return False
            q.append(count[num] - openG)
            prev = num
            openG = count[num]
            if len(q) == groupSize:
                openG -= q.popleft()                

        return openG == 0
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        count = Counter(hand)
        minH = list(count.keys())
        heapq.heapify(minH)
        
        while minH:
            start = heapq.heappop(minH)
            if not count[start]:
                continue

            for i in range(start, start + groupSize):
                if not count[i]:
                    return False
                count[i] -= 1
            
            # Restore minH if start is beg of another sequence 
            if count[start]:
                heapq.heappush(minH, start)

        return True
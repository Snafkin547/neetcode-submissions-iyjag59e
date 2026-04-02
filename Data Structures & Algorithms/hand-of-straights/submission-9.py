class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = groupSize
        if len(hand) < n or len(hand)%n!=0:
            return False
        
        hMap = collections.Counter(hand)
        minHeap = list(hMap.keys())
        heapq.heapify(minHeap)
        while minHeap:
            small = minHeap[0]
            if hMap[small] == 0:
                heapq.heappop(minHeap)
                continue
            size = hMap[small]
            for i in range(small, small + groupSize):
                hMap[i] -= size
                if hMap[i] < 0:
                    return False

        return True
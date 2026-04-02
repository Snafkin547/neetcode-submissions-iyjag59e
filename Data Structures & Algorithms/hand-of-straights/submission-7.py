class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = groupSize
        if len(hand)%n!=0:
            return False
        size = int(len(hand)//n)
        hMap = collections.Counter(hand)
        first, second = [], []
        isFirst = True
        for h in hMap:
            heapq.heappush(first, (h, hMap[h]))
        
        for _ in range(size):
            currH = first if isFirst else second
            nextH = second if isFirst else first
            prev = heapq.heappop(currH)
            prev = (prev[0], prev[1]-1)
            cnt = 1
            while cnt < n and currH:
                this = heapq.heappop(currH)
                # Check if this node is valid (+1)
                if prev[0] + 1 != this[0]:
                    return False
                else:
                    if prev[1]> 0: # Have the prev back to the queue
                       heapq.heappush(nextH, (prev[0], prev[1]))
                    prev = (this[0], this[1]-1)
                    cnt += 1
            if prev[1] > 0:
                heapq.heappush(nextH, prev)
            while currH:
                temp = heapq.heappop(currH)
                heapq.heappush(nextH, temp)
                
            isFirst = False if isFirst else True

        return not first and not second
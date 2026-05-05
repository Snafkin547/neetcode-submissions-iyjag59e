class MedianFinder:

    def __init__(self):
        self.first, self.second = [], []
        self.count = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.first, -num)
        self.count += 1
        if self.count == 1:
            return
        
        heapq.heappush(self.second, -heapq.heappop(self.first))
        heapq.heappush(self.first, -heapq.heappop(self.second))
        
        if len(self.first) > self.count//2:
            heapq.heappush(self.second, -heapq.heappop(self.first))

    def findMedian(self) -> float:
        if self.count == 1:
            return -self.first[0]
        if self.count%2 == 1:
            return self.second[0]
        else:
            return (-self.first[0] + self.second[0])/2
        
        
class MedianFinder:

    def __init__(self):
        self.first, self.second = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.first, -num)
        heapq.heappush(self.second, -heapq.heappop(self.first))
        
        if len(self.first) < len(self.second):
            heapq.heappush(self.first, -heapq.heappop(self.second))
            

    def findMedian(self) -> float:
        if len(self.first) != len(self.second):
            return -self.first[0]
        else:
            return (-self.first[0] + self.second[0])/2
        
        
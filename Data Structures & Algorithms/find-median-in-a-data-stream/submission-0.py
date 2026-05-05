class MedianFinder:

    def __init__(self):
        # Maintain two heaps and count
        self.first = []
        self.second = []
        self.count = 0

    def addNum(self, num: int) -> None:
        # Append to first
        heapq.heappush(self.first, num)
        self.count += 1
        if self.count == 1:
            return

        # If len(first) > count//2: first -> second
        if len(self.first) > self.count //2:
            heapq.heappush(self.second, self.first.pop())
        
        # Always maintain first[-1] < second[0]: check and pop if num is greater
        if self.first[-1] > self.second[0]:
            temp1, temp2 = self.first.pop(), heapq.heappop(self.second)
            self.first.append(temp2)
            heapq.heappush(self.second, temp1)

        # First [1, 2]
        # Second [3, 4, 5]
        # Count 5

    def findMedian(self) -> float:
        if self.count == 0:
            return float('-inf')
        elif self.count == 1:
            return float(self.first[0])
        # When odd: return second[0] unless count == 1
        elif self.count%2 == 1:
            return float(self.second[0])
        # When even: return ave of first[-1] and second[0]
        else:
            return (self.first[-1] + self.second[0])/2
        
        
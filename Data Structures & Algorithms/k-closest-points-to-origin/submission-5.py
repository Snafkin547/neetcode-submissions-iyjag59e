class MinHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, val):
        self.heap.append(val)
        self.bubble_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return
        if len(self.heap) == 1:
            return self.heap.pop()

        popped = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.bubble_down(0)
        return popped

    def bubble_down(self, idx):
        if not self.heap:
            return
        while True:
            smallest = idx
            l = idx * 2 + 1
            r = idx * 2 + 2
            if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
                smallest = l
            if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
                smallest = r

            if idx != smallest:
                self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
                idx = smallest
            else:
                break
        return
    
    def bubble_up(self, idx):
        while True:
            parent = (idx - 1)//2
            if parent >= 0 and self.heap[idx] < self.heap[parent]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break
        return

    def peek(self):
        return self.heap[0] if self.heap else None

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        ''' 
        1) Make A
        # map{dist: list of points}
        # A list of negative distance
        # A heap from the list
        2) Pop furthest if len > k
        3) Return the list of k
        '''
        mh = MinHeap()
        for x, y in points:
            dis = - (x*x + y*y)
            mh.push((dis, [x, y]))
            if len(mh.heap) > k: # Remove to be unused items
                mh.pop()
        return [point for (dist, point) in mh.heap]
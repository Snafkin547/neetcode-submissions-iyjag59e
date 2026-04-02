class MinHeap:
    def __init__(self):
        self.heap = []
    
    def heapify(self, arr):
        self.heap = list(arr)
        n = len(self.heap)
        for i in range(n//2 - 1, -1, -1):
            self.bubble_down(i)
    
    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.bubble_down(0)
        return root
        
    def push(self, val):
        self.heap.append(val)
        n = len(self.heap) - 1
        self.bubble_up(n)
    
    def bubble_up(self, idx):
        parent = (idx - 1)//2
        if idx > 0 and self.heap[parent] > self.heap[idx]:
            self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
            self.bubble_up(parent)
    
    def bubble_down(self, idx):
        left, right = idx * 2 + 1, idx * 2 + 2
        smallest = idx
        if left < len(self.heap) and self.heap[smallest] > self.heap[left]:
            smallest = left
        if right < len(self.heap) and self.heap[smallest] > self.heap[right]:
            smallest = right
        if idx != smallest:
            self.heap[smallest], self.heap[idx] = self.heap[idx], self.heap[smallest]
            self.bubble_down(smallest)
    
    def peek(self):
        return self.heap[0] if self.heap else None


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.mh = MinHeap()
        self.mh.heapify(nums)
        self.k = k
        while len(self.mh.heap) > self.k:
            self.mh.pop()

    def add(self, val: int) -> int:
        self.mh.push(val)
        while len(self.mh.heap) > self.k:
            self.mh.pop()
        return self.mh.heap[0]
        

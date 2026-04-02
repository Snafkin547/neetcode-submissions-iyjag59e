class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Keep whats next in heap
        # if nothing in heap and everything in queue, get the head
        # Regardless, if a head of the queue is ready to be executed, put it back to the heap

        # This system works, because we keep any executables in heap. And when heap is empty, it updates the clock and that'll enforce pushing back mechanism
        
        tasks = Counter(tasks)
        maxH = [-c for c in tasks.values()]
        heapq.heapify(maxH)

        res = 0
        q = deque()
        while maxH or q:
            res += 1
            if maxH:
                t = heapq.heappop(maxH) + 1
                if t != 0:
                    q.append((t, res + n))
            else:
                res = q[0][1]

            if q and q[0][1] == res:
                heapq.heappush(maxH, q.popleft()[0])

        return res
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count each tasks
        count = collections.defaultdict(int)
        for task in tasks:
            count[task] -= 1

        # Make a maxHeap with neg counts
        maxHeap = []
        for task in count:
            heapq.heappush(maxHeap, (count[task], task))

        res = 0
        while True:
            reserve = []
            lim = n + 1
            # Increment res
            while lim > 0:
                if not maxHeap:
                    break
                else:
                    popped = heapq.heappop(maxHeap)
                    updatedCount = popped[0] + 1
                    res += 1
                    if updatedCount < 0:
                        reserve.append((updatedCount, popped[1]))
                    lim -= 1
            # Push items back
            for r in reserve:
                heapq.heappush(maxHeap, r)
            # Determine if continue
            if not maxHeap:
                break
            elif lim > 0:
                res += lim
                
        return res
        

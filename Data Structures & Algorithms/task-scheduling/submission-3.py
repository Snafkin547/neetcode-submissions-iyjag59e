import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count each tasks & Make a maxHeap with neg counts
        maxHeap = [-c for c in Counter(tasks).values()]
        heapq.heapify(maxHeap)

        res = 0

        while maxHeap:
            reserve = []
            # Increment res
            for _ in range(n + 1):
                if maxHeap:
                    popped = heapq.heappop(maxHeap)
                    if popped + 1 < 0:
                        reserve.append(popped + 1)
                res += 1
            
                # Determine if continue
                if not maxHeap and not reserve:
                    break

            # Push items back
            for r in reserve:
                heapq.heappush(maxHeap, r)
        return res
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count each tasks & Make a maxHeap with neg counts
        maxHeap = [-c for c in Counter(tasks).values()]
        heapq.heapify(maxHeap)

        res = 0
        q = deque()
        while q or maxHeap:
            res += 1
            if not maxHeap:
                res = q[0][1] # Jump to the post cooldown timestamp
            else:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    q.append([cnt, res + n])
            
            if q and q[0][1] == res:
                heapq.heappush(maxHeap, q.popleft()[0])
        return res

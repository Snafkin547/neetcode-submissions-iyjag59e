class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = []
        tsk = Counter(tasks)
        
        for c in tsk.values():
            heapq.heappush(count, -c)

        res = 0
        q = deque()
        while count or q:
            res += 1
            if not count:
                res = q[0][1]
            else:
                cnt = heapq.heappop(count) + 1
                if cnt:
                    q.append([cnt, res + n])
            if q and q[0][1] == res:
                heapq.heappush(count, q.popleft()[0])
        return res
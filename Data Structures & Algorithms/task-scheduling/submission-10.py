class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = []
        tsk = Counter(tasks)
        
        for c in tsk.values():
            heapq.heappush(count, -c)

        res = 0
        while count:
            cnt = 0
            temp = []
            for i in range(min(n + 1, len(count))):
                c = heapq.heappop(count)
                res += 1
                cnt += 1
                if c < -1:
                    temp.append(c + 1)
            
            for t in temp:
                heapq.heappush(count, t)

            if count and cnt <= n:
                res += n - cnt + 1
       
        return res
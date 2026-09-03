class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        curr = 0
        readyq = [] # -bal
        waitq = [] # cy, -bal

        _tasks = Counter(tasks)
        for _, v in _tasks.items():
            heapq.heappush(readyq, -v)

        while readyq or waitq:
            while waitq and waitq[0][0] <= curr + 1:
                _, bal = heapq.heappop(waitq)
                heapq.heappush(readyq, bal)

            if readyq:
                bal= heapq.heappop(readyq)
                curr += 1
                if bal < -1:
                    heapq.heappush(waitq, (curr + n + 1, bal + 1))
            else:
                cy, bal = heapq.heappop(waitq)
                curr = max(curr + 1, cy)
                if bal < -1:
                    heapq.heappush(waitq, (curr + n + 1, bal + 1))

        return curr

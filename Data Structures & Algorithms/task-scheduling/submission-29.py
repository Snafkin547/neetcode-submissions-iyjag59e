class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        curr = 0
        taskq = [] # -bal
        waitq = [] # cy, -bal

        _tasks = Counter(tasks)
        for _, v in _tasks.items():
            heapq.heappush(taskq, -v)

        while taskq or waitq:
            if not waitq and taskq:
                bal= heapq.heappop(taskq)
                curr += 1
                if bal < -1:
                    heapq.heappush(waitq, (curr + n + 1, bal + 1))
            elif waitq and not taskq:
                cy, bal = heapq.heappop(waitq)
                curr = max(curr + 1, cy)
                if bal < -1:
                    heapq.heappush(waitq, (curr + n + 1, bal + 1))
            else:
                if waitq[0][1] < taskq[0] and waitq[0][0] <= curr + 1:
                    cy, bal = heapq.heappop(waitq)
                    curr += 1
                    if bal < -1:
                        heapq.heappush(waitq, (curr + 1 + n, bal + 1))

                else:
                    bal = heapq.heappop(taskq)
                    curr += 1
                    if bal < -1:
                        heapq.heappush(waitq, (curr + 1 + n, bal + 1))
        return curr

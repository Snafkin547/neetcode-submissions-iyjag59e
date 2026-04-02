import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count gaps needed
        # Subtract slots that existing tasks can fill (count of each)
        # return he # of task types + remaining idle if exists
        count = [c for c in Counter(tasks).values()]
        # count = [0] * 26
        # for task in tasks:
        #     count[ord(task) - ord('A')] += 1
        count.sort()
        maxf = count[-1]
        idle = (maxf - 1) * n
        for i in range(len(count)-2, -1, -1):
            idle -= min(count[i], maxf - 1)
        return max(0, idle) + len(tasks)
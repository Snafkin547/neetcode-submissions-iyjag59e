import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count gaps needed
        # Subtract slots that existing tasks can fill (count of each)
        # return he # of task types + remaining idle if exists
        # The use of list directly is more efficient due to opverhead by Map
        count = [0]*26
        for t in tasks:
            count[ord(t) - ord('A')] += 1
        maxf = max(count)
        res = 0
        for i in count:
            res += 1 if i == maxf else 0
        time = (maxf - 1) * (n + 1) + res
        return max(len(tasks), time)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for t in tasks:
            count[ord(t) - ord('A')] += 1

        x = max(count)
        extra = 0
        for i in count:
            extra += 1 if x == i else 0
        time = (x - 1) * (n + 1) + extra
        return max(len(tasks), time)

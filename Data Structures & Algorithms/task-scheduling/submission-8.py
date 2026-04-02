import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count gaps needed
        # You need (maxf - 1) times of (n + 1) cycles + the number of task type that consumes the highest frequency
        # The addition of the number of task type that consumes the highest frequency is necessary for the final round : A__A__A__(this)
        # The use of list directly is more efficient due to opverhead by Map
        count = [0] * 26
        for t in tasks:
            count[ord(t) - ord('A')]+=1
        maxf = max(count)
        suffix = 0
        for c in count:
            suffix += 1 if c == maxf else 0
        cycle = (maxf - 1) * (n + 1) + suffix
        return max(len(tasks), cycle)
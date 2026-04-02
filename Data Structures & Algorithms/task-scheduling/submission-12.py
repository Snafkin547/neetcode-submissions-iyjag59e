class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for t in tasks:
            freq[ord(t)-ord('A')] += 1
        
        freq.sort()
        maxf = freq[-1]
        idle = (maxf-1)*n
        for i in range(24,-1,-1):
            idle-=min(maxf-1, freq[i])
        return len(tasks) + max(0, idle)
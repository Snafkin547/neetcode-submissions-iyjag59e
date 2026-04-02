class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for t in tasks:
            freq[ord(t)-ord('A')] += 1
        
        maxf = max(freq)
        num_maxf = 0
        for f in freq:
            num_maxf += 1 if f == maxf else 0
            
        time = (maxf - 1) * (n + 1) + num_maxf
        
        return max(len(tasks), time)
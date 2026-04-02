class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        memo = [0] * n
        memo[0] = 1
        intervals.sort(key=lambda x:x[1])
        
        def bs(r, target):
            l = 0
            while l < r:
                m = l + ((r - l) >> 1)
                if intervals[m][1] <= target:
                    l = m + 1
                else:
                    r = m
            return l

        for i in range(1, n):
            # Find the first fail after i
            idx = bs(i, intervals[i][0])
            if idx == 0: # No relevant
                memo[i] = memo[i - 1]
            else:
                memo[i] = max(memo[i - 1], memo[idx - 1] + 1)
        return n - memo[n - 1]
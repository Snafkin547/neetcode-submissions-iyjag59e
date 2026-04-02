#DP Bottom Up
#DP Binary Search
# Greedy Sort By start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        memo = [0] * n # Store max number of non overlapping so far
        memo[0] = 1
        intervals.sort(key=lambda x:x[1])
        def bs(r, target): # Look for the first fail(After the target)
            l = 0
            while l < r:
                mid = l + ((r - l)>>1)
                if intervals[mid][1] <= target:
                    l = mid + 1
                else:
                    r = mid
            return l

        for i in range(1, n):
            idx = bs(i, intervals[i][0])
            if idx == 0:
                memo[i] = memo[i -1]
            else: # Compare with the last successful index(idx - 1) bc idx failed
                memo[i] = max(memo[i - 1], memo[idx - 1] + 1)
        return n - memo[n - 1]
            